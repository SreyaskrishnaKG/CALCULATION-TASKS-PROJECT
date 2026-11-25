from django.shortcuts import render
from django.views.generic import View
import json
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

@method_decorator(csrf_exempt,name='dispatch')   
class BMIView(View):
    def post(self,request):
        data=json.loads(request.body)
        h=data.get("height")
        w=data.get("weight")
        
        HEIGHT=h/100
        
        BMI_=w/HEIGHT**2
        
        result ={
            "HEIGHT":data.get("height"),
            "WEIGHT":data.get("weight"),
            "BMI":round(BMI_,2)
        }
        return JsonResponse(result)
    
       
@method_decorator(csrf_exempt,name='dispatch')     
class Agecal_view(View):
    def post(self,request):
        info=json.loads(request.body)
        birth=info.get("birth_year")
        current=info.get("current_year")
        
        age=current-birth
        
        return JsonResponse({
            "BIRTH":info.get("birth_year"),
            "CURRENT_AGE":age
            
        })
        
        

@method_decorator(csrf_exempt,name='dispatch')
class PercentView(View):
    def post(self,request):
        info=json.loads(request.body)
        obtained=info.get("obtained_marks")
        total=info.get("total_marks")
        
        percent=(obtained/total)*100
        
        result={"PERCENT":percent    
        }
        
        return JsonResponse(result)
    
    

@method_decorator(csrf_exempt,name='dispatch')
class SI_View(View):
    def post(self,request):
        info=json.loads(request.body)
        p=info.get("principle")
        r=info.get("rate")
        t=info.get("time")
        SI=(p*r*t)/100
        return JsonResponse({
            "Principle":info.get("principle"),
            "rate":r,
            "time":t,
            "SIMPLE_INTEREST":SI
        })
        

@method_decorator(csrf_exempt,name='dispatch')
class ElectricityView(View):
    def post(self,request):
        info=json.loads(request.body)
        u=info.get("units")
        r=info.get("rate")
        bill=(u*r)
        return JsonResponse({
            "Units":u,
            "Rate":r,
            "Bill":bill
        })
        
        
@method_decorator(csrf_exempt,name='dispatch')        
class DiscountView(View):
    def post(self,request):
        info=json.loads(request.body)
        p=info.get("price")
        dis=info.get("discount_percentage")
        dis_amount=(p*dis)/100
        final=p-dis_amount
        return JsonResponse({
            "Price":p,
            "Discount_percentage":dis,
            "Discount_amount":dis_amount,
            "Final_price":final
        })
        
@method_decorator(csrf_exempt,name='dispatch')
class ProfitView(View):
    def post(self,request):
        info=json.loads(request.body)
        cost=info.get("cost_price")
        sell=info.get("selling_price")
        profit=sell-cost
        result={
            "Cost_price":cost,
            "Selling_price":sell,
            "Profit  ":profit
        }
        return JsonResponse(result)
@method_decorator(csrf_exempt,name='dispatch')
class Salary(View):
    def post(self,request):
        info=json.loads(request.body)
        basic=info.get("basic_salary")
        bonus=info.get("bonus")
        dedu=info.get("deduction")
        net=(basic+bonus)-dedu
        
        return JsonResponse({
            "Basic_salary":basic,
            "Bonus":bonus,
            "Deduction":dedu,
            "Net salary":net
        })
        
@method_decorator(csrf_exempt,name='dispatch')
class TimeView(View):
    def post(self,request):
        info=json.loads(request.body)
        h=info.get("hours")
        m=h*6
        s=h*3600
        return JsonResponse({
            "Hours":h,
            "Minute":m,
            "Seconds":s
        })
    
@method_decorator(csrf_exempt,name='dispatch')
class FuelView(View):
    def post(self,request):
        info=json.loads(request.body)
        d=info.get("distance")
        m=info.get("mileage")
        f_price=info.get("fuel_price")
        f_required=d/m
        total=f_required*f_price
        return JsonResponse({
            "Distance":d,
            "Mileage":m,
            "Fuel_price":f_price,
            "Fuel_required":f_required,
            "Total_cost":total
            
        })
        
        
@method_decorator(csrf_exempt,name='dispatch')
class ProductView(View):
    def post(self,request):
        info=json.loads(request.body)
        cost=info.get("cost_price")
        sell=info.get("selling_price")
        quan=info.get("quantity")
        total_c=cost*quan
        total_s=sell*quan
        profit=total_s-total_c
        
        result={
            "Cost_price":cost,
            "Selling_price":sell,
            "Quantity":quan,
            "Total_cost":total_c,
            "Total_sales":total_s,
            "Profit":profit
        }
        return JsonResponse(result)
  
  
    
@method_decorator(csrf_exempt,name='dispatch')
class WorkView(View):
    def post(self,request):
        info=json.loads(request.body)
        hours_w=info.get("hours_worked")
        hours_regu=info.get("regular_hours")
        hours_rate=info.get("hourly_rate")
        over_timerate=info.get("overtime_rate")
        overtime_hours=hours_w-hours_regu
        regu_pay=hours_regu * hours_rate
        overtime_pay= overtime_hours * over_timerate
        total_salary=regu_pay + overtime_pay
        
        result={
            "hours_worked": hours_w,
            "regular_hours": hours_regu,
            "hourly_rate": hours_rate,
            "overtime_rate": over_timerate,
            "regular_pay": regu_pay,
            "overtime_hours": overtime_hours,
            "overtime_pay": overtime_pay,
            "Total_salary": total_salary
        }
        
        return JsonResponse(result)
    

@method_decorator(csrf_exempt,name='dispatch')   
class AgeView(View):
    def post(self,request):
        info=json.loads(request.body)
        age=info.get("age")
        month=age*12
        weeks=age*52
        days=age*365
        return JsonResponse({
            
            "Age": age,
            "Months": month,
            "Weeks": weeks,
            "Days": days

        })
        
        
    