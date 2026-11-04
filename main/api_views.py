from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.authentication import SessionAuthentication
from rest_framework.decorators import (
    api_view, authentication_classes, permission_classes,
)
from rest_framework.response import Response

from main.models import Skill
from main.permissions import IsPortfolioOwnerOrEditorOrReadOnly
from main.serializers import SkillSerializer
from rest_framework.permissions import IsAuthenticated


@api_view(["GET", "HEAD", "POST"])
@authentication_classes([SessionAuthentication])
@permission_classes([IsPortfolioOwnerOrEditorOrReadOnly])
def skill_list(request):
    if request.method in ("GET", "HEAD"):
        skills = Skill.objects.prefetch_related(
            "starred_by"
        ).order_by("name", "id")

        name = request.query_params.get("name", "").strip()
        if name:
            skills = skills.filter(name__icontains=name)

        serializer = SkillSerializer(
            skills, many=True, context={"request": request},
        )
        return Response(serializer.data)

    serializer = SkillSerializer(
        data=request.data, context={"request": request}
    )
    serializer.is_valid(raise_exception=True)
    serializer.save()

    return Response(
        serializer.data,
        status=status.HTTP_201_CREATED
    )

@api_view(["GET", "HEAD", "PUT", "PATCH", "DELETE"])
@authentication_classes([SessionAuthentication])
@permission_classes([IsPortfolioOwnerOrEditorOrReadOnly])
def skill_detail(request, skill_id):
    skill = get_object_or_404(
        Skill.objects.prefetch_related("starred_by"),
        pk=skill_id,
    )

    if request.method in ("GET", "HEAD"):
        serializer = SkillSerializer(
            skill,
            context={"request": request},
        )
        return Response(serializer.data)

    if request.method == "DELETE":
        skill.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    serializer = SkillSerializer(
        skill,
        data=request.data,
        partial=request.method == "PATCH",
        context={"request": request},
    )
    serializer.is_valid(raise_exception=True)
    serializer.save()

    return Response(serializer.data)

@api_view(["POST"])
@authentication_classes([SessionAuthentication])
@permission_classes([IsAuthenticated])
def skill_star(request, skill_id):
    skill = get_object_or_404(Skill, pk=skill_id)

    if skill.starred_by.filter(pk=request.user.pk).exists():
        skill.starred_by.remove(request.user)
    else:
        skill.starred_by.add(request.user)

    serializer = SkillSerializer(
        skill,
        context={"request": request}
    )
    return Response(serializer.data)