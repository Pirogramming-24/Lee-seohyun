#메인화면에보이는?,,

from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Count
from django.http import JsonResponse
from django.views.decorators.http import require_POST

from .models import Idea, DevTool, IdeaStar
from .forms import IdeaForm, DevToolForm



def devtool_list(request):
    devtools = DevTool.objects.all().order_by("name")
    return render(request, "devtools/devtool_list.html", {"devtools": devtools})


def devtool_create(request):
    if request.method == "POST":
        form = DevToolForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("idea_site:devtool_list")
    else:
        form = DevToolForm()
    return render(request, "devtools/devtool_form.html", {"form": form})


def devtool_detail(request, pk):
    tool = get_object_or_404(DevTool, pk=pk)
    ideas = Idea.objects.filter(devtool=tool).order_by("-created_at")
    return render(request, "devtools/devtool_detail.html", {"tool": tool, "ideas": ideas})


def devtool_update(request, pk):
    tool = get_object_or_404(DevTool, pk=pk)
    if request.method == "POST":
        form = DevToolForm(request.POST, instance=tool)
        if form.is_valid():
            form.save()
            return redirect("idea_site:devtool_detail", pk=tool.pk)
    else:
        form = DevToolForm(instance=tool)
    return render(request, "devtools/devtool_form.html", {"form": form, "tool": tool})


def devtool_delete(request, pk):
    tool = get_object_or_404(DevTool, pk=pk)
    if request.method == "POST":
        tool.delete()
        return redirect("idea_site:devtool_list")
    return render(request, "confirm.html", {"object": tool})


def idea_list(request):
    sort = request.GET.get("sort", "latest")

    qs = Idea.objects.select_related("devtool").annotate(star_count=Count("stars"))

    if sort == "name":
        qs = qs.order_by("title")
    elif sort == "oldest":
        qs = qs.order_by("created_at")
    elif sort == "stars":
        qs = qs.order_by("-star_count", "-created_at")
    else:
        qs = qs.order_by("-created_at")

    if not request.session.session_key:
        request.session.save()
    sk = request.session.session_key

    starred_ids = set(
        IdeaStar.objects.filter(session_key=sk).values_list("idea_id", flat=True)
    )

    return render(request, "ideas/idea_list.html", {"ideas": qs, "sort": sort, "starred_ids": starred_ids})


def idea_detail(request, pk):
    idea = get_object_or_404(
        Idea.objects.select_related("devtool").annotate(star_count=Count("stars")),
        pk=pk
    )

    if not request.session.session_key:
        request.session.save()
    sk = request.session.session_key
    starred = IdeaStar.objects.filter(idea_id=pk, session_key=sk).exists()

    return render(request, "ideas/idea_detail.html", {"idea": idea, "starred": starred})


def idea_create(request):
    if request.method == "POST":
        form = IdeaForm(request.POST, request.FILES)
        if form.is_valid():
            idea = form.save()
            return redirect("idea_site:idea_detail", pk=idea.pk)
    else:
        form = IdeaForm()
    return render(request, "ideas/idea_form.html", {"form": form, "mode": "create"})


def idea_update(request, pk):
    idea = get_object_or_404(Idea, pk=pk)

    if request.method == "POST":
        form = IdeaForm(request.POST, request.FILES, instance=idea)
        if form.is_valid():
            idea = form.save()
            return redirect("idea_site:idea_detail", pk=idea.pk)
    else:
        form = IdeaForm(instance=idea)

    return render(request, "ideas/idea_form.html", {"form": form, "mode": "update", "idea": idea})


def idea_delete(request, pk):
    idea = get_object_or_404(Idea, pk=pk)
    if request.method == "POST":
        idea.delete()
        return redirect("idea_site:idea_list")
    return render(request, "ideas/confirm_delete.html", {"object": idea})


#찜
@require_POST
def idea_star_toggle(request, pk):
    idea = get_object_or_404(Idea, pk=pk)

    if not request.session.session_key:
        request.session.save()
    sk = request.session.session_key

    star = IdeaStar.objects.filter(idea=idea, session_key=sk).first()
    if star:
        star.delete()
    else:
        IdeaStar.objects.create(idea=idea, session_key=sk)

    return redirect(request.META.get("HTTP_REFERER", "idea_site:idea_list"))