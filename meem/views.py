from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

def check_age(request):
    if request.method == "GET":
        age = request.GET.get("age")
        if age is not None:
            try :
                age=int(age)
                if age >= 18:
                    return JsonResponse({"age" : age, "is_adult" : True, "message" : "you are adult"})
                else:
                    return JsonResponse({"age" : age, "is_adult" : False, "message" : "you are not adult"})
            except ValueError:
                return JsonResponse({"error": "Your age should be intager"}, status=400)
        return JsonResponse({"message": "Please provide your age"})
    return JsonResponse({"error": "Only for get option"}, status=405)

def regions(request):
    uzb_regions = {
        "andijon", "buxoro", "fargona", "jizzax", "namangan",
        "navoiy", "qashqadaryo", "samarqand", "surxondaryo",
        "sirdaryo", "xorazm", "toshkent", "qoraqalpogiston"
    }
    
    if request.method == "GET":
        region = request.get("region", "").strip().lower()
        if region:
            exists = region in uzb_regions
            return JsonResponse({"region": region, "exists_in_uzbekistan": exists})
        return JsonResponse({"message" : "Please enter your region"})
    return JsonResponse({"error" : "Only for get option "}, status = 405)
       
# Create your views here.
