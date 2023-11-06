from django.shortcuts import render
from medico.views import DocReviews
from django.http import JsonResponse

import time
import asyncio
import random


# Create your views here.


def index(request):
    return render(request, 'index.html', context={'text': 'hello world xx'})


async def testAsyncProviderDocReviews(data, nro, tinit, *args, **kwargs):
    t = [0, 0, 0, 0, 0, 0, 0]
    t[0] = time.time_ns()/1000000
    queryset = DocReviews.x_get_queryset(kwargs["medico"])
    t[1] = time.time_ns()/1000000
    await asyncio.sleep(0)
#   aux = await queryset.afirst()
    async for review in queryset.values():
        #       await asyncio.sleep(0.001)
        review["aatime"] = time.time_ns()/1000000 - tinit
        review["aanro"] = nro
        data.append(review)
    t[2] = time.time_ns()/1000000
    x = [0, t[1]-t[0], t[2]-t[1]]
    return True


async def asyncPrueba(*args, **kwargs):
    data = []
    initTime = time.time_ns()/1000000
    execs = [testAsyncProviderDocReviews(
        data, nro, initTime, (), medico=random.randrange(31)) for nro in range(1, 3000)]
    total = asyncio.gather(*execs)
    initTime = time.time_ns()/1000000
    results = await total
    return data


async def asyncProviderDocReviews(*args, **kwargs):
    queryset = DocReviews.x_get_queryset(kwargs["medico"])
    data = [review async for review in queryset.values()]
    return data


async def asyncDocReviews(request, *args, **kwargs):
    data = await asyncProviderDocReviews(*args, **kwargs)
    return JsonResponse(data, safe=False)
