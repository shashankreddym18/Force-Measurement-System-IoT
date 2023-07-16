from datetime import datetime
import random
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from .forms import StudentForm
from .models import StudentModel, readings
from serial import Serial
import struct


def add_student(request, template_name='student_add.html'):
    form = StudentForm(request.POST or None)
    if form.is_valid():
        form.save()
        return  HttpResponse("ok saved")
        return redirect('Student:student_manage')
    return render(request, template_name, {'form':form})


def student_manage(request, template_name='student_manage.html'):
    std_data = StudentModel.objects.all() 
    data = {}
    data['object_list'] = std_data
    return render(request, template_name, data)


def student_edit(request, pk, template_name='student_add.html'):
    book= get_object_or_404(StudentModel, pk=pk)
    form = StudentForm(request.POST or None, instance=book)
    if form.is_valid():
        form.save()
        return redirect('Student:student_manage')
    return render(request, template_name, {'form':form})

def delete_student(request, pk):
    obj = get_object_or_404(StudentModel, pk=pk)
    obj.delete()
    return redirect('Student:student_manage')



def show_graph(request,template_name='live_graph.html'):
    return render(request,template_name)


def fetch_sensor_values_ajax(request):
    data={}
    float_val=0.0
    if request.is_ajax():
            com_port = request.GET.get('id', None)
            sensor_val=random.random() 
            sensor_data=[]
            now=datetime.now()
            ok_date=str(now.strftime('%Y-%m-%d %H:%M:%S'))
            try:
                sr=Serial(com_port,9600)
                st=list(str(sr.readline(),'utf-8'))
                sr.close()
                hex_str = str(''.join(st[:]))
                sensor_val=str(hex_str)
             
                if(sensor_val):
                    print(sensor_val)
                    sensor_data.append(str(sensor_val)+','+ok_date)
                    sensor_val2 = int(float_val)
                    savy = readings(sensor_data = sensor_val2,time = ok_date)
                    
                else:
                    sensor_data.append(str(sensor_val)+','+ok_date)
                    sensor_val2 = int(float_val)
                    savy = readings(sensor_data = sensor_val2,time = ok_date)
                    
            except Exception as e:
                    sensor_data.append(str(sensor_val)+','+ok_date)
                    sensor_val2 = int(float_val)
                    savy = readings(sensor_data = sensor_val2,time = ok_date)
                    
            data['result']=sensor_data
    else:
        data['result']='Not Ajax'
    return JsonResponse(data)
