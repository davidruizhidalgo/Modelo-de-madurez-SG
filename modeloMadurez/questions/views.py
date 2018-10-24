from django.template.defaultfilters import slugify
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.shortcuts import redirect
from django.urls import reverse, reverse_lazy
from .models import Questionary
from .forms import QuestionaryForm, QuestionaryUpdateForm

# Create your views here.
class QuestionaryListView(ListView):
    model = Questionary

class QuestionaryDetailView(DetailView):
    model = Questionary
    template_name_suffix = '_detail'


#############################################################
#################################################################
class ResultsDetailView(DetailView):
    model = Questionary
    template_name_suffix = '_detail_result'
    data_act = []
    data_p1 = []
    data_p2 = []
    prom_data_act = []
    prom_data_p1 = []
    prom_data_p2 = []
    
    def get_table_data_srm(self):
        table_data = [] #lista vacia para almacenar resultados 
        #############SMR#################
        #smr 1.1 
        if self.object.srm_11_act == 'D': 
            table_data.append(0.4*1.0)
        elif self.object.srm_11_act == 'C':
            table_data.append(0.4*0.7)
        elif self.object.srm_11_act == 'B':
            table_data.append(0.4*0.5)
        else: # A o nulo
            table_data.append(0.0)

        if self.object.srm_11_p1 == 'D': 
            table_data.append(0.4*1.0)
        elif self.object.srm_11_p1 == 'C':
            table_data.append(0.4*0.7)
        elif self.object.srm_11_p1 == 'B':
            table_data.append(0.4*0.5)
        else: # A o nulo
            table_data.append(0.0)
  
        if self.object.srm_11_p2 == 'D': 
            table_data.append(0.4*1.0)
        elif self.object.srm_11_p2 == 'C':
            table_data.append(0.4*0.7)
        elif self.object.srm_11_p2 == 'B':
            table_data.append(0.4*0.5)
        else: # A o nulo
            table_data.append(0.0)

        #smr 1.2 
        if self.object.srm_12_act == 'E': 
            table_data.append(0.35*1.0)
        elif self.object.srm_12_act == 'D': 
            table_data.append(0.35*7.0)
        elif self.object.srm_12_act == 'C':
            table_data.append(0.35*0.55)
        elif self.object.srm_12_act == 'B':
            table_data.append(0.35*0.4)
        else: # A o nulo
            table_data.append(0.0)

        if self.object.srm_12_p1 == 'E': 
            table_data.append(0.35*1.0)
        elif self.object.srm_12_p1 == 'D': 
            table_data.append(0.35*0.7)
        elif self.object.srm_12_p1 == 'C':
            table_data.append(0.35*0.55)
        elif self.object.srm_12_p1 == 'B':
            table_data.append(0.35*0.4)
        else: # A o nulo
            table_data.append(0.0)

        if self.object.srm_12_p2 == 'E': 
            table_data.append(0.35*1.0)
        elif self.object.srm_12_p2 == 'D': 
            table_data.append(0.35*7.0)
        elif self.object.srm_12_p2 == 'C':
            table_data.append(0.35*0.55)
        elif self.object.srm_12_p2 == 'B':
            table_data.append(0.35*0.4)
        else: # A o nulo
            table_data.append(0.0)

        #smr 1.3
        if self.object.srm_13_act == 'C': 
            table_data.append(0.25*1.0)
        elif self.object.srm_13_act == 'B': 
            table_data.append(0.25*7.0)
        else: # A o nulo
            table_data.append(0.0)

        if self.object.srm_13_p1 == 'C': 
            table_data.append(0.25*1.0)
        elif self.object.srm_13_p1 == 'B': 
            table_data.append(0.25*7.0)
        else: # A o nulo
            table_data.append(0.0)

        if self.object.srm_13_p2 == 'C': 
            table_data.append(0.25*1.0)
        elif self.object.srm_13_p2 == 'B': 
            table_data.append(0.25*7.0)
        else: # A o nulo
            table_data.append(0.0)

        #smr 2.1 
        if self.object.srm_21_act == 'D': 
            table_data.append(0.3*1.0)
        elif self.object.srm_21_act == 'C':
            table_data.append(0.3*0.7)
        elif self.object.srm_21_act == 'B':
            table_data.append(0.3*0.5)
        else: # A o nulo
            table_data.append(0.0)

        if self.object.srm_21_p1 == 'D': 
            table_data.append(0.3*1.0)
        elif self.object.srm_21_p1 == 'C':
            table_data.append(0.3*0.7)
        elif self.object.srm_21_p1 == 'B':
            table_data.append(0.3*0.5)
        else: # A o nulo
            table_data.append(0.0)
  
        if self.object.srm_21_p2 == 'D': 
            table_data.append(0.3*1.0)
        elif self.object.srm_21_p2 == 'C':
            table_data.append(0.3*0.7)
        elif self.object.srm_21_p2 == 'B':
            table_data.append(0.3*0.5)
        else: # A o nulo
            table_data.append(0.0)

        #smr 2.2 
        if self.object.srm_22_act == 'D': 
            table_data.append(0.15*1.0)
        elif self.object.srm_22_act == 'C':
            table_data.append(0.15*0.7)
        elif self.object.srm_22_act == 'B':
            table_data.append(0.15*0.5)
        else: # A o nulo
            table_data.append(0.0)

        if self.object.srm_22_p1 == 'D': 
            table_data.append(0.15*1.0)
        elif self.object.srm_22_p1 == 'C':
            table_data.append(0.15*0.7)
        elif self.object.srm_22_p1 == 'B':
            table_data.append(0.15*0.5)
        else: # A o nulo
            table_data.append(0.0)
  
        if self.object.srm_22_p2 == 'D': 
            table_data.append(0.15*1.0)
        elif self.object.srm_22_p2 == 'C':
            table_data.append(0.15*0.7)
        elif self.object.srm_22_p2 == 'B':
            table_data.append(0.15*0.5)
        else: # A o nulo
            table_data.append(0.0)

        #smr 2.3 
        if self.object.srm_23_act == 'D': 
            table_data.append(0.10*1.0)
        elif self.object.srm_23_act == 'C':
            table_data.append(0.10*0.7)
        elif self.object.srm_23_act == 'B':
            table_data.append(0.10*0.5)
        else: # A o nulo
            table_data.append(0.0)

        if self.object.srm_23_p1 == 'D': 
            table_data.append(0.10*1.0)
        elif self.object.srm_23_p1 == 'C':
            table_data.append(0.10*0.7)
        elif self.object.srm_23_p1 == 'B':
            table_data.append(0.10*0.5)
        else: # A o nulo
            table_data.append(0.0)
  
        if self.object.srm_23_p2 == 'D': 
            table_data.append(0.10*1.0)
        elif self.object.srm_23_p2 == 'C':
            table_data.append(0.10*0.7)
        elif self.object.srm_23_p2 == 'B':
            table_data.append(0.10*0.5)
        else: # A o nulo
            table_data.append(0.0)

        #smr 2.4
        if self.object.srm_24_act == 'D': 
            table_data.append(0.10*1.0)
        elif self.object.srm_24_act == 'C':
            table_data.append(0.10*0.55)
        elif self.object.srm_24_act == 'B':
            table_data.append(0.10*0.3)
        else: # A o nulo
            table_data.append(0.0)

        if self.object.srm_24_p1 == 'D': 
            table_data.append(0.10*1.0)
        elif self.object.srm_24_p1 == 'C':
            table_data.append(0.10*0.55)
        elif self.object.srm_24_p1 == 'B':
            table_data.append(0.10*0.3)
        else: # A o nulo
            table_data.append(0.0)
  
        if self.object.srm_24_p2 == 'D': 
            table_data.append(0.10*1.0)
        elif self.object.srm_24_p2 == 'C':
            table_data.append(0.10*0.55)
        elif self.object.srm_24_p2 == 'B':
            table_data.append(0.10*0.3)
        else: # A o nulo
            table_data.append(0.0)

        #smr 2.5 
        if self.object.srm_25_act == 'D': 
            table_data.append(0.20*1.0)
        elif self.object.srm_25_act == 'C':
            table_data.append(0.20*0.7)
        elif self.object.srm_25_act == 'B':
            table_data.append(0.20*0.5)
        else: # A o nulo
            table_data.append(0.0)

        if self.object.srm_25_p1 == 'D': 
            table_data.append(0.20*1.0)
        elif self.object.srm_25_p1 == 'C':
            table_data.append(0.20*0.7)
        elif self.object.srm_25_p1 == 'B':
            table_data.append(0.20*0.5)
        else: # A o nulo
            table_data.append(0.0)
  
        if self.object.srm_25_p2 == 'D': 
            table_data.append(0.20*1.0)
        elif self.object.srm_25_p2 == 'C':
            table_data.append(0.20*0.7)
        elif self.object.srm_25_p2 == 'B':
            table_data.append(0.20*0.5)
        else: # A o nulo
            table_data.append(0.0)
        #smr 2.6
        if self.object.srm_26_act == 'E': 
            table_data.append(0.15*1.0)
        elif self.object.srm_26_act == 'D':
            table_data.append(0.15*0.7)
        elif self.object.srm_26_act == 'C':
            table_data.append(0.15*0.5)
        elif self.object.srm_26_act == 'B':
            table_data.append(0.15*0.3)
        else: # A o nulo
            table_data.append(0.0)

        if self.object.srm_26_p1 == 'E': 
            table_data.append(0.15*1.0)
        elif self.object.srm_26_p1 == 'D':
            table_data.append(0.15*0.7)
        elif self.object.srm_26_p1 == 'C':
            table_data.append(0.15*0.5)
        elif self.object.srm_26_p1 == 'B':
            table_data.append(0.15*0.3)
        else: # A o nulo
            table_data.append(0.0)
  
        if self.object.srm_26_p2 == 'E': 
            table_data.append(0.15*1.0)
        elif self.object.srm_26_p2 == 'D':
            table_data.append(0.15*0.7)
        elif self.object.srm_26_p2 == 'C':
            table_data.append(0.15*0.5)
        elif self.object.srm_26_p2 == 'B':
            table_data.append(0.15*0.3)
        else: # A o nulo
            table_data.append(0.0)

                #smr 3.1
        if self.object.srm_31_act == 'D': 
            table_data.append(0.4*1.0)
        elif self.object.srm_31_act == 'C':
            table_data.append(0.4*0.7)
        elif self.object.srm_31_act == 'B':
            table_data.append(0.40*0.3)
        else: # A o nulo
            table_data.append(0.0)

        if self.object.srm_31_p1 == 'D': 
            table_data.append(0.4*1.0)
        elif self.object.srm_31_p1 == 'C':
            table_data.append(0.4*0.7)
        elif self.object.srm_31_p1 == 'B':
            table_data.append(0.4*0.3)
        else: # A o nulo
            table_data.append(0.0)
  
        if self.object.srm_31_p2 == 'D': 
            table_data.append(0.4*1.0)
        elif self.object.srm_31_p2 == 'C':
            table_data.append(0.4*0.7)
        elif self.object.srm_31_p2 == 'B':
            table_data.append(0.4*0.3)
        else: # A o nulo
            table_data.append(0.0)

        #smr 3.2
        if self.object.srm_32_act == 'D': 
            table_data.append(0.3*1.0)
        elif self.object.srm_32_act == 'C':
            table_data.append(0.3*0.7)
        elif self.object.srm_32_act == 'B':
            table_data.append(0.30*0.5)
        else: # A o nulo
            table_data.append(0.0)

        if self.object.srm_32_p1 == 'D': 
            table_data.append(0.3*1.0)
        elif self.object.srm_32_p1 == 'C':
            table_data.append(0.3*0.7)
        elif self.object.srm_32_p1 == 'B':
            table_data.append(0.3*0.5)
        else: # A o nulo
            table_data.append(0.0)
  
        if self.object.srm_32_p2 == 'D': 
            table_data.append(0.3*1.0)
        elif self.object.srm_32_p2 == 'C':
            table_data.append(0.3*0.7)
        elif self.object.srm_32_p2 == 'B':
            table_data.append(0.3*0.5)
        else: # A o nulo
            table_data.append(0.0)

        #smr 3.3
        if self.object.srm_33_act == 'D': 
            table_data.append(0.2*1.0)
        elif self.object.srm_33_act == 'C':
            table_data.append(0.2*0.7)
        elif self.object.srm_33_act == 'B':
            table_data.append(0.20*0.2)
        else: # A o nulo
            table_data.append(0.0)

        if self.object.srm_33_p1 == 'D': 
            table_data.append(0.2*1.0)
        elif self.object.srm_33_p1 == 'C':
            table_data.append(0.2*0.7)
        elif self.object.srm_33_p1 == 'B':
            table_data.append(0.2*0.2)
        else: # A o nulo
            table_data.append(0.0)
  
        if self.object.srm_33_p2 == 'D': 
            table_data.append(0.2*1.0)
        elif self.object.srm_33_p2 == 'C':
            table_data.append(0.2*0.7)
        elif self.object.srm_33_p2 == 'B':
            table_data.append(0.2*0.2)
        else: # A o nulo
            table_data.append(0.0)

        #smr 3.4
        if self.object.srm_34_act == 'D': 
            table_data.append(0.1*1.0)
        elif self.object.srm_34_act == 'C':
            table_data.append(0.1*0.6)
        elif self.object.srm_34_act == 'B':
            table_data.append(0.10*0.2)
        else: # A o nulo
            table_data.append(0.0)

        if self.object.srm_34_p1 == 'D': 
            table_data.append(0.1*1.0)
        elif self.object.srm_34_p1 == 'C':
            table_data.append(0.1*0.6)
        elif self.object.srm_34_p1 == 'B':
            table_data.append(0.1*0.2)
        else: # A o nulo
            table_data.append(0.0)
  
        if self.object.srm_34_p2 == 'D': 
            table_data.append(0.1*1.0)
        elif self.object.srm_34_p2 == 'C':
            table_data.append(0.1*0.6)
        elif self.object.srm_34_p2 == 'B':
            table_data.append(0.1*0.2)
        else: # A o nulo
            table_data.append(0.0)

        #smr 4.1
        if self.object.srm_41_act == 'D': 
            table_data.append(0.35*1.0)
        elif self.object.srm_41_act == 'C':
            table_data.append(0.35*0.7)
        elif self.object.srm_41_act == 'B':
            table_data.append(0.35*0.5)
        else: # A o nulo
            table_data.append(0.0)

        if self.object.srm_41_p1 == 'D': 
            table_data.append(0.35*1.0)
        elif self.object.srm_41_p1 == 'C':
            table_data.append(0.35*0.7)
        elif self.object.srm_41_p1 == 'B':
            table_data.append(0.35*0.5)
        else: # A o nulo
            table_data.append(0.0)
  
        if self.object.srm_41_p2 == 'D': 
            table_data.append(0.35*1.0)
        elif self.object.srm_41_p2 == 'C':
            table_data.append(0.35*0.7)
        elif self.object.srm_41_p2 == 'B':
            table_data.append(0.35*0.5)
        else: # A o nulo
            table_data.append(0.0)

        #smr 4.2
        if self.object.srm_42_act == 'D': 
            table_data.append(0.35*1.0)
        elif self.object.srm_42_act == 'C':
            table_data.append(0.35*0.7)
        elif self.object.srm_42_act == 'B':
            table_data.append(0.35*0.5)
        else: # A o nulo
            table_data.append(0.0)

        if self.object.srm_42_p1 == 'D': 
            table_data.append(0.35*1.0)
        elif self.object.srm_42_p1 == 'C':
            table_data.append(0.35*0.7)
        elif self.object.srm_42_p1 == 'B':
            table_data.append(0.35*0.5)
        else: # A o nulo
            table_data.append(0.0)
  
        if self.object.srm_42_p2 == 'D': 
            table_data.append(0.35*1.0)
        elif self.object.srm_42_p2 == 'C':
            table_data.append(0.35*0.7)
        elif self.object.srm_42_p2 == 'B':
            table_data.append(0.35*0.5)
        else: # A o nulo
            table_data.append(0.0)

        #smr 4.3
        if self.object.srm_43_act == 'D': 
            table_data.append(0.3*1.0)
        elif self.object.srm_43_act == 'C':
            table_data.append(0.3*0.7)
        elif self.object.srm_43_act == 'B':
            table_data.append(0.3*0.5)
        else: # A o nulo
            table_data.append(0.0)

        if self.object.srm_43_p1 == 'D': 
            table_data.append(0.3*1.0)
        elif self.object.srm_43_p1 == 'C':
            table_data.append(0.3*0.7)
        elif self.object.srm_43_p1 == 'B':
            table_data.append(0.3*0.5)
        else: # A o nulo
            table_data.append(0.0)
  
        if self.object.srm_43_p2 == 'D': 
            table_data.append(0.3*1.0)
        elif self.object.srm_43_p2 == 'C':
            table_data.append(0.3*0.7)
        elif self.object.srm_43_p2 == 'B':
            table_data.append(0.3*0.5)
        else: # A o nulo
            table_data.append(0.0)

        #smr 5.1
        if self.object.srm_51_act == 'D': 
            table_data.append(0.35*1.0)
        elif self.object.srm_51_act == 'C':
            table_data.append(0.35*0.5)
        elif self.object.srm_51_act == 'B':
            table_data.append(0.35*0.3)
        else: # A o nulo
            table_data.append(0.0)

        if self.object.srm_51_p1 == 'D': 
            table_data.append(0.35*1.0)
        elif self.object.srm_51_p1 == 'C':
            table_data.append(0.35*0.5)
        elif self.object.srm_51_p1 == 'B':
            table_data.append(0.35*0.3)
        else: # A o nulo
            table_data.append(0.0)
  
        if self.object.srm_51_p2 == 'D': 
            table_data.append(0.35*1.0)
        elif self.object.srm_51_p2 == 'C':
            table_data.append(0.35*0.5)
        elif self.object.srm_51_p2 == 'B':
            table_data.append(0.35*0.3)
        else: # A o nulo
            table_data.append(0.0)

        #smr 5.2
        if self.object.srm_52_act == 'F': 
            table_data.append(0.3*1.0)
        elif self.object.srm_52_act == 'E':
            table_data.append(0.3*0.8)
        elif self.object.srm_52_act == 'D':
            table_data.append(0.3*0.6)
        elif self.object.srm_52_act == 'C':
            table_data.append(0.3*0.4)
        elif self.object.srm_52_act == 'B':
            table_data.append(0.3*0.1)
        else: # A o nulo
            table_data.append(0.0)

        if self.object.srm_52_p1 == 'F': 
            table_data.append(0.3*1.0)
        elif self.object.srm_52_p1 == 'E':
            table_data.append(0.3*0.8)
        elif self.object.srm_52_p1 == 'D':
            table_data.append(0.3*0.6)
        elif self.object.srm_52_p1 == 'C':
            table_data.append(0.3*0.4)
        elif self.object.srm_52_p1 == 'B':
            table_data.append(0.3*0.1)
        else: # A o nulo
            table_data.append(0.0)
  
        if self.object.srm_52_p2 == 'F': 
            table_data.append(0.3*1.0)
        elif self.object.srm_52_p2 == 'E':
            table_data.append(0.3*0.8)
        elif self.object.srm_52_p2 == 'D':
            table_data.append(0.3*0.6)
        elif self.object.srm_52_p2 == 'C':
            table_data.append(0.3*0.4)
        elif self.object.srm_52_p2 == 'B':
            table_data.append(0.3*0.1)
        else: # A o nulo
            table_data.append(0.0)
        #smr 5.3
        if self.object.srm_53_act == 'D': 
            table_data.append(0.35*1.0)
        elif self.object.srm_53_act == 'C':
            table_data.append(0.35*0.5)
        elif self.object.srm_53_act == 'B':
            table_data.append(0.35*0.2)
        else: # A o nulo
            table_data.append(0.0)

        if self.object.srm_53_p1 == 'D': 
            table_data.append(0.35*1.0)
        elif self.object.srm_53_p1 == 'C':
            table_data.append(0.35*0.5)
        elif self.object.srm_53_p1 == 'B':
            table_data.append(0.35*0.2)
        else: # A o nulo
            table_data.append(0.0)
  
        if self.object.srm_53_p2 == 'D': 
            table_data.append(0.35*1.0)
        elif self.object.srm_53_p2 == 'C':
            table_data.append(0.35*0.5)
        elif self.object.srm_53_p2 == 'B':
            table_data.append(0.35*0.2)
        else: # A o nulo
            table_data.append(0.0)    
        
        return table_data

    def get_table_data_os(self):
        table_data = [] #lista vacia para almacenar resultados 
        #############OS#################
                #os 1.1
        if self.object.os_11_act == 'C': 
            table_data.append(0.33*1.0)
        elif self.object.os_11_act == 'B':
            table_data.append(0.33*0.7)
        else: # A o nulo
            table_data.append(0.0)

        if self.object.os_11_p1 == 'C': 
            table_data.append(0.33*1.0)
        elif self.object.os_11_p1 == 'B':
            table_data.append(0.33*0.7)
        else: # A o nulo
            table_data.append(0.0)
  
        if self.object.os_11_p2 == 'C': 
            table_data.append(0.33*1.0)
        elif self.object.os_11_p2 == 'B':
            table_data.append(0.33*0.7)
        else: # A o nulo
            table_data.append(0.0)

        #os 1.2
        if self.object.os_12_act == 'C': 
            table_data.append(0.33*1.0)
        elif self.object.os_12_act == 'B':
            table_data.append(0.33*0.6)
        else: # A o nulo
            table_data.append(0.0)

        if self.object.os_12_p1 == 'C': 
            table_data.append(0.33*1.0)
        elif self.object.os_12_p1 == 'B':
            table_data.append(0.33*0.6)
        else: # A o nulo
            table_data.append(0.0)
  
        if self.object.os_12_p2 == 'C': 
            table_data.append(0.33*1.0)
        elif self.object.os_12_p2 == 'B':
            table_data.append(0.33*0.6)
        else: # A o nulo
            table_data.append(0.0)

        #os 1.3
        if self.object.os_13_act == 'D': 
            table_data.append(0.34*1.0)
        elif self.object.os_13_act == 'C':
            table_data.append(0.34*0.7)
        elif self.object.os_13_act == 'B':
            table_data.append(0.34*0.5)
        else: # A o nulo
            table_data.append(0.0)

        if self.object.os_13_p1 == 'D': 
            table_data.append(0.34*1.0)
        elif self.object.os_13_p1 == 'C':
            table_data.append(0.34*0.7)
        elif self.object.os_13_p1 == 'B':
            table_data.append(0.34*0.5)
        else: # A o nulo
            table_data.append(0.0)
  
        if self.object.os_13_p2 == 'D': 
            table_data.append(0.34*1.0)
        elif self.object.os_13_p2 == 'C':
            table_data.append(0.34*0.7)
        elif self.object.os_13_p2 == 'B':
            table_data.append(0.34*0.5)
        else: # A o nulo
            table_data.append(0.0)
        #os 2.1
        if self.object.os_21_act == 'D': 
            table_data.append(0.25*1.0)
        elif self.object.os_21_act == 'C':
            table_data.append(0.25*0.7)
        elif self.object.os_21_act == 'B':
            table_data.append(0.25*0.5)
        else: # A o nulo
            table_data.append(0.0)

        if self.object.os_21_p1 == 'D': 
            table_data.append(0.25*1.0)
        elif self.object.os_21_p1 == 'C':
            table_data.append(0.25*0.7)
        elif self.object.os_21_p1 == 'B':
            table_data.append(0.25*0.5)
        else: # A o nulo
            table_data.append(0.0)
  
        if self.object.os_21_p2 == 'D': 
            table_data.append(0.25*1.0)
        elif self.object.os_21_p2 == 'C':
            table_data.append(0.25*0.7)
        elif self.object.os_21_p2 == 'B':
            table_data.append(0.25*0.5)
        else: # A o nulo
            table_data.append(0.0)

        #os 2.2
        if self.object.os_22_act == 'D': 
            table_data.append(0.22*1.0)
        elif self.object.os_22_act == 'C':
            table_data.append(0.22*0.7)
        elif self.object.os_22_act == 'B':
            table_data.append(0.22*0.5)
        else: # A o nulo
            table_data.append(0.0)

        if self.object.os_22_p1 == 'D': 
            table_data.append(0.22*1.0)
        elif self.object.os_22_p1 == 'C':
            table_data.append(0.22*0.7)
        elif self.object.os_22_p1 == 'B':
            table_data.append(0.22*0.5)
        else: # A o nulo
            table_data.append(0.0)
  
        if self.object.os_22_p2 == 'D': 
            table_data.append(0.22*1.0)
        elif self.object.os_22_p2 == 'C':
            table_data.append(0.22*0.7)
        elif self.object.os_22_p2 == 'B':
            table_data.append(0.22*0.5)
        else: # A o nulo
            table_data.append(0.0)

        #os 2.3
        if self.object.os_23_act == 'D': 
            table_data.append(0.22*1.0)
        elif self.object.os_23_act == 'C':
            table_data.append(0.22*0.7)
        elif self.object.os_23_act == 'B':
            table_data.append(0.22*0.4)
        else: # A o nulo
            table_data.append(0.0)

        if self.object.os_23_p1 == 'D': 
            table_data.append(0.22*1.0)
        elif self.object.os_23_p1 == 'C':
            table_data.append(0.22*0.7)
        elif self.object.os_23_p1 == 'B':
            table_data.append(0.22*0.4)
        else: # A o nulo
            table_data.append(0.0)
  
        if self.object.os_23_p2 == 'D': 
            table_data.append(0.22*1.0)
        elif self.object.os_23_p2 == 'C':
            table_data.append(0.22*0.7)
        elif self.object.os_23_p2 == 'B':
            table_data.append(0.22*0.4)
        else: # A o nulo
            table_data.append(0.0)

        #os 2.4
        if self.object.os_24_act == 'D': 
            table_data.append(0.15*0.8)
        elif self.object.os_24_act == 'C':
            table_data.append(0.15*0.5)
        elif self.object.os_24_act == 'B':
            table_data.append(0.15*0.3)
        else: # A o nulo
            table_data.append(0.0)

        if self.object.os_24_p1 == 'D': 
            table_data.append(0.15*0.8)
        elif self.object.os_24_p1 == 'C':
            table_data.append(0.15*0.5)
        elif self.object.os_24_p1 == 'B':
            table_data.append(0.15*0.3)
        else: # A o nulo
            table_data.append(0.0)
  
        if self.object.os_24_p2 == 'D': 
            table_data.append(0.15*0.8)
        elif self.object.os_24_p2 == 'C':
            table_data.append(0.15*0.5)
        elif self.object.os_24_p2 == 'B':
            table_data.append(0.15*0.3)
        else: # A o nulo
            table_data.append(0.0)

        #os 2.5
        if self.object.os_25_act == 'D': 
            table_data.append(0.16*1.0)
        elif self.object.os_25_act == 'C':
            table_data.append(0.16*0.7)
        elif self.object.os_25_act == 'B':
            table_data.append(0.16*0.5)
        else: # A o nulo
            table_data.append(0.0)

        if self.object.os_25_p1 == 'D': 
            table_data.append(0.16*1.0)
        elif self.object.os_25_p1 == 'C':
            table_data.append(0.16*0.7)
        elif self.object.os_25_p1 == 'B':
            table_data.append(0.16*0.5)
        else: # A o nulo
            table_data.append(0.0)
  
        if self.object.os_25_p2 == 'D': 
            table_data.append(0.15*1.0)
        elif self.object.os_25_p2 == 'C':
            table_data.append(0.15*0.7)
        elif self.object.os_25_p2 == 'B':
            table_data.append(0.15*0.5)
        else: # A o nulo
            table_data.append(0.0)

       #os 3.1
        if self.object.os_31_act == 'E': 
            table_data.append(0.25*1.0)
        elif self.object.os_31_act == 'D':
            table_data.append(0.25*0.7)
        elif self.object.os_31_act == 'C':
            table_data.append(0.25*0.5)
        elif self.object.os_31_act == 'B':
            table_data.append(0.25*0.3)
        else: # A o nulo
            table_data.append(0.0)

        if self.object.os_31_p1 == 'E': 
            table_data.append(0.25*1.0)
        elif self.object.os_31_p1 == 'D':
            table_data.append(0.25*0.7)
        elif self.object.os_31_p1 == 'C':
            table_data.append(0.25*0.5)
        elif self.object.os_31_p1 == 'B':
            table_data.append(0.25*0.3)
        else: # A o nulo
            table_data.append(0.0)
  
        if self.object.os_31_p2 == 'E': 
            table_data.append(0.25*1.0)
        elif self.object.os_31_p2 == 'D':
            table_data.append(0.25*0.7)
        elif self.object.os_31_p2 == 'C':
            table_data.append(0.25*0.5)
        elif self.object.os_31_p2 == 'B':
            table_data.append(0.25*0.3)
        else: # A o nulo
            table_data.append(0.0)
       #os 3.2
        if self.object.os_32_act == 'E': 
            table_data.append(0.2*1.0)
        elif self.object.os_32_act == 'D':
            table_data.append(0.2*0.7)
        elif self.object.os_32_act == 'C':
            table_data.append(0.2*0.5)
        elif self.object.os_32_act == 'B':
            table_data.append(0.2*0.3)
        else: # A o nulo
            table_data.append(0.0)

        if self.object.os_32_p1 == 'E': 
            table_data.append(0.2*1.0)
        elif self.object.os_32_p1 == 'D':
            table_data.append(0.2*0.7)
        elif self.object.os_32_p1 == 'C':
            table_data.append(0.2*0.5)
        elif self.object.os_32_p1 == 'B':
            table_data.append(0.2*0.3)
        else: # A o nulo
            table_data.append(0.0)
  
        if self.object.os_32_p2 == 'E': 
            table_data.append(0.2*1.0)
        elif self.object.os_32_p2 == 'D':
            table_data.append(0.2*0.7)
        elif self.object.os_32_p2 == 'C':
            table_data.append(0.2*0.5)
        elif self.object.os_32_p2 == 'B':
            table_data.append(0.2*0.3)
        else: # A o nulo
            table_data.append(0.0)
       #os 3.3
        if self.object.os_33_act == 'E': 
            table_data.append(0.1*1.0)
        elif self.object.os_33_act == 'D':
            table_data.append(0.1*0.7)
        elif self.object.os_33_act == 'C':
            table_data.append(0.1*0.5)
        elif self.object.os_33_act == 'B':
            table_data.append(0.1*0.3)
        else: # A o nulo
            table_data.append(0.0)

        if self.object.os_33_p1 == 'E': 
            table_data.append(0.1*1.0)
        elif self.object.os_33_p1 == 'D':
            table_data.append(0.1*0.7)
        elif self.object.os_33_p1 == 'C':
            table_data.append(0.1*0.5)
        elif self.object.os_33_p1 == 'B':
            table_data.append(0.1*0.3)
        else: # A o nulo
            table_data.append(0.0)
  
        if self.object.os_33_p2 == 'E': 
            table_data.append(0.1*1.0)
        elif self.object.os_33_p2 == 'D':
            table_data.append(0.1*0.7)
        elif self.object.os_33_p2 == 'C':
            table_data.append(0.1*0.5)
        elif self.object.os_33_p2 == 'B':
            table_data.append(0.1*0.3)
        else: # A o nulo
            table_data.append(0.0)
        #os 3.4
        if self.object.os_34_act == 'D': 
            table_data.append(0.2*1.0)
        elif self.object.os_34_act == 'C':
            table_data.append(0.2*0.7)
        elif self.object.os_34_act == 'B':
            table_data.append(0.2*0.5)
        else: # A o nulo
            table_data.append(0.0)

        if self.object.os_34_p1 == 'D': 
            table_data.append(0.2*1.0)
        elif self.object.os_34_p1 == 'C':
            table_data.append(0.2*0.7)
        elif self.object.os_34_p1 == 'B':
            table_data.append(0.2*0.5)
        else: # A o nulo
            table_data.append(0.0)
  
        if self.object.os_34_p2 == 'D': 
            table_data.append(0.2*1.0)
        elif self.object.os_34_p2 == 'C':
            table_data.append(0.2*0.7)
        elif self.object.os_34_p2 == 'B':
            table_data.append(0.2*0.5)
        else: # A o nulo
            table_data.append(0.0)
        
               #os 3.5
        if self.object.os_35_act == 'E': 
            table_data.append(0.1*1.0)
        elif self.object.os_35_act == 'D':
            table_data.append(0.1*0.7)
        elif self.object.os_35_act == 'C':
            table_data.append(0.1*0.3)
        elif self.object.os_35_act == 'B':
            table_data.append(0.1*0.1)
        else: # A o nulo
            table_data.append(0.0)

        if self.object.os_35_p1 == 'E': 
            table_data.append(0.1*1.0)
        elif self.object.os_35_p1 == 'D':
            table_data.append(0.1*0.7)
        elif self.object.os_35_p1 == 'C':
            table_data.append(0.1*0.3)
        elif self.object.os_35_p1 == 'B':
            table_data.append(0.1*0.1)
        else: # A o nulo
            table_data.append(0.0)
  
        if self.object.os_35_p2 == 'E': 
            table_data.append(0.1*1.0)
        elif self.object.os_35_p2 == 'D':
            table_data.append(0.1*0.7)
        elif self.object.os_35_p2 == 'C':
            table_data.append(0.1*0.3)
        elif self.object.os_35_p2 == 'B':
            table_data.append(0.1*0.1)
        else: # A o nulo
            table_data.append(0.0)
        #os 3.6
        if self.object.os_36_act == 'D': 
            table_data.append(0.15*1.0)
        elif self.object.os_36_act == 'C':
            table_data.append(0.15*0.7)
        elif self.object.os_36_act == 'B':
            table_data.append(0.15*0.5)
        else: # A o nulo
            table_data.append(0.0)

        if self.object.os_36_p1 == 'D': 
            table_data.append(0.15*1.0)
        elif self.object.os_36_p1 == 'C':
            table_data.append(0.15*0.7)
        elif self.object.os_36_p1 == 'B':
            table_data.append(0.15*0.5)
        else: # A o nulo
            table_data.append(0.0)
  
        if self.object.os_36_p2 == 'D': 
            table_data.append(0.15*1.0)
        elif self.object.os_36_p2 == 'C':
            table_data.append(0.15*0.7)
        elif self.object.os_36_p2 == 'B':
            table_data.append(0.15*0.5)
        else: # A o nulo
            table_data.append(0.0)

        #os 4.1
        if self.object.os_41_act == 'D': 
            table_data.append(0.33*1.0)
        elif self.object.os_41_act == 'C':
            table_data.append(0.33*0.7)
        elif self.object.os_41_act == 'B':
            table_data.append(0.33*0.5)
        else: # A o nulo
            table_data.append(0.0)

        if self.object.os_41_p1 == 'D': 
            table_data.append(0.33*1.0)
        elif self.object.os_41_p1 == 'C':
            table_data.append(0.33*0.7)
        elif self.object.os_41_p1 == 'B':
            table_data.append(0.33*0.5)
        else: # A o nulo
            table_data.append(0.0)
  
        if self.object.os_41_p2 == 'D': 
            table_data.append(0.33*1.0)
        elif self.object.os_41_p2 == 'C':
            table_data.append(0.33*0.7)
        elif self.object.os_41_p2 == 'B':
            table_data.append(0.33*0.5)
        else: # A o nulo
            table_data.append(0.0)

        #os 4.2
        if self.object.os_42_act == 'D': 
            table_data.append(0.33*1.0)
        elif self.object.os_42_act == 'C':
            table_data.append(0.33*0.7)
        elif self.object.os_42_act == 'B':
            table_data.append(0.33*0.5)
        else: # A o nulo
            table_data.append(0.0)

        if self.object.os_42_p1 == 'D': 
            table_data.append(0.33*1.0)
        elif self.object.os_42_p1 == 'C':
            table_data.append(0.33*0.7)
        elif self.object.os_42_p1 == 'B':
            table_data.append(0.33*0.5)
        else: # A o nulo
            table_data.append(0.0)
  
        if self.object.os_42_p2 == 'D': 
            table_data.append(0.33*1.0)
        elif self.object.os_42_p2 == 'C':
            table_data.append(0.33*0.7)
        elif self.object.os_42_p2 == 'B':
            table_data.append(0.33*0.5)
        else: # A o nulo
            table_data.append(0.0)
        #os 4.3
        if self.object.os_43_act == 'D': 
            table_data.append(0.34*1.0)
        elif self.object.os_43_act == 'C':
            table_data.append(0.34*0.7)
        elif self.object.os_43_act == 'B':
            table_data.append(0.34*0.4)
        else: # A o nulo
            table_data.append(0.0)

        if self.object.os_43_p1 == 'D': 
            table_data.append(0.34*1.0)
        elif self.object.os_43_p1 == 'C':
            table_data.append(0.34*0.7)
        elif self.object.os_43_p1 == 'B':
            table_data.append(0.34*0.4)
        else: # A o nulo
            table_data.append(0.0)
  
        if self.object.os_43_p2 == 'D': 
            table_data.append(0.34*1.0)
        elif self.object.os_43_p2 == 'C':
            table_data.append(0.34*0.7)
        elif self.object.os_43_p2 == 'B':
            table_data.append(0.34*0.4)
        else: # A o nulo
            table_data.append(0.0)
        #os 5.1
        if self.object.os_51_act == 'D': 
            table_data.append(0.4*1.0)
        elif self.object.os_51_act == 'C':
            table_data.append(0.4*0.7)
        elif self.object.os_51_act == 'B':
            table_data.append(0.4*0.5)
        else: # A o nulo
            table_data.append(0.0)

        if self.object.os_51_p1 == 'D': 
            table_data.append(0.4*1.0)
        elif self.object.os_51_p1 == 'C':
            table_data.append(0.4*0.7)
        elif self.object.os_51_p1 == 'B':
            table_data.append(0.4*0.5)
        else: # A o nulo
            table_data.append(0.0)
  
        if self.object.os_51_p2 == 'D': 
            table_data.append(0.4*1.0)
        elif self.object.os_51_p2 == 'C':
            table_data.append(0.4*0.7)
        elif self.object.os_51_p2 == 'B':
            table_data.append(0.4*0.5)
        else: # A o nulo
            table_data.append(0.0)

        #os 5.2
        if self.object.os_52_act == 'D': 
            table_data.append(0.4*1.0)
        elif self.object.os_52_act == 'C':
            table_data.append(0.4*0.7)
        elif self.object.os_52_act == 'B':
            table_data.append(0.4*0.5)
        else: # A o nulo
            table_data.append(0.0)

        if self.object.os_52_p1 == 'D': 
            table_data.append(0.4*1.0)
        elif self.object.os_52_p1 == 'C':
            table_data.append(0.4*0.7)
        elif self.object.os_52_p1 == 'B':
            table_data.append(0.4*0.5)
        else: # A o nulo
            table_data.append(0.0)
  
        if self.object.os_52_p2 == 'D': 
            table_data.append(0.4*1.0)
        elif self.object.os_52_p2 == 'C':
            table_data.append(0.4*0.7)
        elif self.object.os_52_p2 == 'B':
            table_data.append(0.4*0.5)
        else: # A o nulo
            table_data.append(0.0)

        #os 5.3
        if self.object.os_53_act == 'D': 
            table_data.append(0.2*1.0)
        elif self.object.os_53_act == 'C':
            table_data.append(0.2*0.7)
        elif self.object.os_53_act == 'B':
            table_data.append(0.2*0.5)
        else: # A o nulo
            table_data.append(0.0)

        if self.object.os_53_p1 == 'D': 
            table_data.append(0.2*1.0)
        elif self.object.os_53_p1 == 'C':
            table_data.append(0.2*0.7)
        elif self.object.os_53_p1 == 'B':
            table_data.append(0.2*0.5)
        else: # A o nulo
            table_data.append(0.0)
  
        if self.object.os_53_p2 == 'D': 
            table_data.append(0.2*1.0)
        elif self.object.os_53_p2 == 'C':
            table_data.append(0.2*0.7)
        elif self.object.os_53_p2 == 'B':
            table_data.append(0.2*0.5)
        else: # A o nulo
            table_data.append(0.0)

        return table_data

    def get_table_data_go(self):
        table_data = [] #lista vacia para almacenar resultados 
        #############GO#################
        #go 1.1
        if self.object.go_11_act == 'D': 
            table_data.append(0.2*1.0)
        elif self.object.go_11_act == 'C':
            table_data.append(0.2*0.7)
        elif self.object.go_11_act == 'B':
            table_data.append(0.2*0.5)
        else: # A o nulo
            table_data.append(0.0)

        if self.object.go_11_p1 == 'D': 
            table_data.append(0.2*1.0)
        elif self.object.go_11_p1 == 'C':
            table_data.append(0.2*0.7)
        elif self.object.go_11_p1 == 'B':
            table_data.append(0.2*0.5)
        else: # A o nulo
            table_data.append(0.0)
  
        if self.object.go_11_p2 == 'D': 
            table_data.append(0.2*1.0)
        elif self.object.go_11_p2 == 'C':
            table_data.append(0.2*0.7)
        elif self.object.go_11_p2 == 'B':
            table_data.append(0.2*0.5)
        else: # A o nulo
            table_data.append(0.0)
        #go 1.2
        if self.object.go_12_act == 'D': 
            table_data.append(0.2*1.0)
        elif self.object.go_12_act == 'C':
            table_data.append(0.2*0.7)
        elif self.object.go_12_act == 'B':
            table_data.append(0.2*0.3)
        else: # A o nulo
            table_data.append(0.0)

        if self.object.go_12_p1 == 'D': 
            table_data.append(0.2*1.0)
        elif self.object.go_12_p1 == 'C':
            table_data.append(0.2*0.7)
        elif self.object.go_12_p1 == 'B':
            table_data.append(0.2*0.3)
        else: # A o nulo
            table_data.append(0.0)
  
        if self.object.go_12_p2 == 'D': 
            table_data.append(0.2*1.0)
        elif self.object.go_12_p2 == 'C':
            table_data.append(0.2*0.7)
        elif self.object.go_12_p2 == 'B':
            table_data.append(0.2*0.3)
        else: # A o nulo
            table_data.append(0.0)
        #go 1.3
        if self.object.go_13_act == 'D': 
            table_data.append(0.2*1.0)
        elif self.object.go_13_act == 'C':
            table_data.append(0.2*0.7)
        elif self.object.go_13_act == 'B':
            table_data.append(0.2*0.3)
        else: # A o nulo
            table_data.append(0.0)

        if self.object.go_13_p1 == 'D': 
            table_data.append(0.2*1.0)
        elif self.object.go_13_p1 == 'C':
            table_data.append(0.2*0.7)
        elif self.object.go_13_p1 == 'B':
            table_data.append(0.2*0.3)
        else: # A o nulo
            table_data.append(0.0)
  
        if self.object.go_13_p2 == 'D': 
            table_data.append(0.2*1.0)
        elif self.object.go_13_p2 == 'C':
            table_data.append(0.2*0.7)
        elif self.object.go_13_p2 == 'B':
            table_data.append(0.2*0.3)
        else: # A o nulo
            table_data.append(0.0)
        #go 1.4
        if self.object.go_14_act == 'D': 
            table_data.append(0.2*1.0)
        elif self.object.go_14_act == 'C':
            table_data.append(0.2*0.7)
        elif self.object.go_14_act == 'B':
            table_data.append(0.2*0.3)
        else: # A o nulo
            table_data.append(0.0)

        if self.object.go_14_p1 == 'D': 
            table_data.append(0.2*1.0)
        elif self.object.go_14_p1 == 'C':
            table_data.append(0.2*0.7)
        elif self.object.go_14_p1 == 'B':
            table_data.append(0.2*0.3)
        else: # A o nulo
            table_data.append(0.0)
  
        if self.object.go_14_p2 == 'D': 
            table_data.append(0.2*1.0)
        elif self.object.go_14_p2 == 'C':
            table_data.append(0.2*0.7)
        elif self.object.go_14_p2 == 'B':
            table_data.append(0.2*0.3)
        else: # A o nulo
            table_data.append(0.0)
        #go 1.5
        if self.object.go_15_act == 'D': 
            table_data.append(0.2*1.0)
        elif self.object.go_15_act == 'C':
            table_data.append(0.2*0.7)
        elif self.object.go_15_act == 'B':
            table_data.append(0.2*0.4)
        else: # A o nulo
            table_data.append(0.0)

        if self.object.go_15_p1 == 'D': 
            table_data.append(0.2*1.0)
        elif self.object.go_15_p1 == 'C':
            table_data.append(0.2*0.7)
        elif self.object.go_15_p1 == 'B':
            table_data.append(0.2*0.4)
        else: # A o nulo
            table_data.append(0.0)
  
        if self.object.go_15_p2 == 'D': 
            table_data.append(0.2*1.0)
        elif self.object.go_15_p2 == 'C':
            table_data.append(0.2*0.7)
        elif self.object.go_15_p2 == 'B':
            table_data.append(0.2*0.4)
        else: # A o nulo
            table_data.append(0.0)
       #go 2.1
        if self.object.go_21_act == 'E': 
            table_data.append(0.27*1.0)
        elif self.object.go_21_act == 'D':
            table_data.append(0.27*0.7)
        elif self.object.go_21_act == 'C':
            table_data.append(0.27*0.5)
        elif self.object.go_21_act == 'B':
            table_data.append(0.27*0.3)
        else: # A o nulo
            table_data.append(0.0)

        if self.object.go_21_p1 == 'E': 
            table_data.append(0.27*1.0)
        elif self.object.go_21_p1 == 'D':
            table_data.append(0.27*0.7)
        elif self.object.go_21_p1 == 'C':
            table_data.append(0.27*0.5)
        elif self.object.go_21_p1 == 'B':
            table_data.append(0.27*0.3)
        else: # A o nulo
            table_data.append(0.0)
  
        if self.object.go_21_p2 == 'E': 
            table_data.append(0.27*1.0)
        elif self.object.go_21_p2 == 'D':
            table_data.append(0.27*0.7)
        elif self.object.go_21_p2 == 'C':
            table_data.append(0.27*0.5)
        elif self.object.go_21_p2 == 'B':
            table_data.append(0.27*0.3)
        else: # A o nulo
            table_data.append(0.0)
        #go 2.2
        if self.object.go_22_act == 'D': 
            table_data.append(0.2*1.0)
        elif self.object.go_22_act == 'C':
            table_data.append(0.2*0.7)
        elif self.object.go_22_act == 'B':
            table_data.append(0.2*0.3)
        else: # A o nulo
            table_data.append(0.0)

        if self.object.go_22_p1 == 'D': 
            table_data.append(0.2*1.0)
        elif self.object.go_22_p1 == 'C':
            table_data.append(0.2*0.7)
        elif self.object.go_22_p1 == 'B':
            table_data.append(0.2*0.3)
        else: # A o nulo
            table_data.append(0.0)
  
        if self.object.go_22_p2 == 'D': 
            table_data.append(0.2*1.0)
        elif self.object.go_22_p2 == 'C':
            table_data.append(0.2*0.7)
        elif self.object.go_22_p2 == 'B':
            table_data.append(0.2*0.3)
        else: # A o nulo
            table_data.append(0.0)
        #go 2.3
        if self.object.go_23_act == 'D': 
            table_data.append(0.26*1.0)
        elif self.object.go_23_act == 'C':
            table_data.append(0.26*0.7)
        elif self.object.go_23_act == 'B':
            table_data.append(0.26*0.3)
        else: # A o nulo
            table_data.append(0.0)

        if self.object.go_23_p1 == 'D': 
            table_data.append(0.26*1.0)
        elif self.object.go_23_p1 == 'C':
            table_data.append(0.26*0.7)
        elif self.object.go_23_p1 == 'B':
            table_data.append(0.26*0.3)
        else: # A o nulo
            table_data.append(0.0)
  
        if self.object.go_23_p2 == 'D': 
            table_data.append(0.26*1.0)
        elif self.object.go_23_p2 == 'C':
            table_data.append(0.26*0.7)
        elif self.object.go_23_p2 == 'B':
            table_data.append(0.26*0.3)
        else: # A o nulo
            table_data.append(0.0)
       #go 2.4
        if self.object.go_24_act == 'E': 
            table_data.append(0.27*1.0)
        elif self.object.go_24_act == 'D':
            table_data.append(0.27*0.7)
        elif self.object.go_24_act == 'C':
            table_data.append(0.27*0.5)
        elif self.object.go_24_act == 'B':
            table_data.append(0.27*0.3)
        else: # A o nulo
            table_data.append(0.0)

        if self.object.go_24_p1 == 'E': 
            table_data.append(0.27*1.0)
        elif self.object.go_24_p1 == 'D':
            table_data.append(0.27*0.7)
        elif self.object.go_24_p1 == 'C':
            table_data.append(0.27*0.5)
        elif self.object.go_24_p1 == 'B':
            table_data.append(0.27*0.3)
        else: # A o nulo
            table_data.append(0.0)
  
        if self.object.go_24_p2 == 'E': 
            table_data.append(0.27*1.0)
        elif self.object.go_24_p2 == 'D':
            table_data.append(0.27*0.7)
        elif self.object.go_24_p2 == 'C':
            table_data.append(0.27*0.5)
        elif self.object.go_24_p2 == 'B':
            table_data.append(0.27*0.3)
        else: # A o nulo
            table_data.append(0.0)
        #go 3.1
        if self.object.go_31_act == 'D': 
            table_data.append(0.18*1.0)
        elif self.object.go_31_act == 'C':
            table_data.append(0.18*0.5)
        elif self.object.go_31_act == 'B':
            table_data.append(0.18*0.3)
        else: # A o nulo
            table_data.append(0.0)

        if self.object.go_31_p1 == 'D': 
            table_data.append(0.18*1.0)
        elif self.object.go_31_p1 == 'C':
            table_data.append(0.18*0.5)
        elif self.object.go_31_p1 == 'B':
            table_data.append(0.18*0.3)
        else: # A o nulo
            table_data.append(0.0)
  
        if self.object.go_31_p2 == 'D': 
            table_data.append(0.18*1.0)
        elif self.object.go_31_p2 == 'C':
            table_data.append(0.18*0.5)
        elif self.object.go_31_p2 == 'B':
            table_data.append(0.18*0.3)
        else: # A o nulo
            table_data.append(0.0)
        #go 3.2
        if self.object.go_32_act == 'D': 
            table_data.append(0.1*1.0)
        elif self.object.go_32_act == 'C':
            table_data.append(0.1*0.7)
        elif self.object.go_32_act == 'B':
            table_data.append(0.1*0.5)
        else: # A o nulo
            table_data.append(0.0)

        if self.object.go_32_p1 == 'D': 
            table_data.append(0.1*1.0)
        elif self.object.go_32_p1 == 'C':
            table_data.append(0.1*0.7)
        elif self.object.go_32_p1 == 'B':
            table_data.append(0.1*0.5)
        else: # A o nulo
            table_data.append(0.0)
  
        if self.object.go_32_p2 == 'D': 
            table_data.append(0.1*1.0)
        elif self.object.go_32_p2 == 'C':
            table_data.append(0.1*0.7)
        elif self.object.go_32_p2 == 'B':
            table_data.append(0.1*0.5)
        else: # A o nulo
            table_data.append(0.0)
       #go 3.3
        if self.object.go_33_act == 'E': 
            table_data.append(0.18*1.0)
        elif self.object.go_33_act == 'D':
            table_data.append(0.18*0.7)
        elif self.object.go_33_act == 'C':
            table_data.append(0.18*0.5)
        elif self.object.go_33_act == 'B':
            table_data.append(0.18*0.2)
        else: # A o nulo
            table_data.append(0.0)

        if self.object.go_33_p1 == 'E': 
            table_data.append(0.18*1.0)
        elif self.object.go_33_p1 == 'D':
            table_data.append(0.18*0.7)
        elif self.object.go_33_p1 == 'C':
            table_data.append(0.18*0.5)
        elif self.object.go_33_p1 == 'B':
            table_data.append(0.18*0.2)
        else: # A o nulo
            table_data.append(0.0)
  
        if self.object.go_33_p2 == 'E': 
            table_data.append(0.18*1.0)
        elif self.object.go_33_p2 == 'D':
            table_data.append(0.18*0.7)
        elif self.object.go_33_p2 == 'C':
            table_data.append(0.18*0.5)
        elif self.object.go_33_p2 == 'B':
            table_data.append(0.18*0.2)
        else: # A o nulo
            table_data.append(0.0)
        #go 3.4
        if self.object.go_34_act == 'D': 
            table_data.append(0.18*1.0)
        elif self.object.go_34_act == 'C':
            table_data.append(0.18*0.5)
        elif self.object.go_34_act == 'B':
            table_data.append(0.18*0.3)
        else: # A o nulo
            table_data.append(0.0)

        if self.object.go_34_p1 == 'D': 
            table_data.append(0.18*1.0)
        elif self.object.go_34_p1 == 'C':
            table_data.append(0.18*0.5)
        elif self.object.go_34_p1 == 'B':
            table_data.append(0.18*0.3)
        else: # A o nulo
            table_data.append(0.0)
  
        if self.object.go_34_p2 == 'D': 
            table_data.append(0.18*1.0)
        elif self.object.go_34_p2 == 'C':
            table_data.append(0.18*0.5)
        elif self.object.go_34_p2 == 'B':
            table_data.append(0.18*0.3)
        else: # A o nulo
            table_data.append(0.0)
       #go 3.5
        if self.object.go_35_act == 'E': 
            table_data.append(0.18*1.0)
        elif self.object.go_35_act == 'D':
            table_data.append(0.18*0.7)
        elif self.object.go_35_act == 'C':
            table_data.append(0.18*0.5)
        elif self.object.go_35_act == 'B':
            table_data.append(0.18*0.3)
        else: # A o nulo
            table_data.append(0.0)

        if self.object.go_35_p1 == 'E': 
            table_data.append(0.18*1.0)
        elif self.object.go_35_p1 == 'D':
            table_data.append(0.18*0.7)
        elif self.object.go_35_p1 == 'C':
            table_data.append(0.18*0.5)
        elif self.object.go_35_p1 == 'B':
            table_data.append(0.18*0.3)
        else: # A o nulo
            table_data.append(0.0)
  
        if self.object.go_35_p2 == 'E': 
            table_data.append(0.18*1.0)
        elif self.object.go_35_p2 == 'D':
            table_data.append(0.18*0.7)
        elif self.object.go_35_p2 == 'C':
            table_data.append(0.18*0.5)
        elif self.object.go_35_p2 == 'B':
            table_data.append(0.18*0.3)
        else: # A o nulo
            table_data.append(0.0)
       #go 3.6
        if self.object.go_36_act == 'E': 
            table_data.append(0.18*1.0)
        elif self.object.go_36_act == 'D':
            table_data.append(0.18*0.7)
        elif self.object.go_36_act == 'C':
            table_data.append(0.18*0.5)
        elif self.object.go_36_act == 'B':
            table_data.append(0.18*0.3)
        else: # A o nulo
            table_data.append(0.0)

        if self.object.go_36_p1 == 'E': 
            table_data.append(0.18*1.0)
        elif self.object.go_36_p1 == 'D':
            table_data.append(0.18*0.7)
        elif self.object.go_36_p1 == 'C':
            table_data.append(0.18*0.5)
        elif self.object.go_36_p1 == 'B':
            table_data.append(0.18*0.3)
        else: # A o nulo
            table_data.append(0.0)
  
        if self.object.go_36_p2 == 'E': 
            table_data.append(0.18*1.0)
        elif self.object.go_36_p2 == 'D':
            table_data.append(0.18*0.7)
        elif self.object.go_36_p2 == 'C':
            table_data.append(0.18*0.5)
        elif self.object.go_36_p2 == 'B':
            table_data.append(0.18*0.3)
        else: # A o nulo
            table_data.append(0.0)
        #go 4.1
        if self.object.go_41_act == 'D': 
            table_data.append(0.2*1.0)
        elif self.object.go_41_act == 'C':
            table_data.append(0.2*0.7)
        elif self.object.go_41_act == 'B':
            table_data.append(0.2*0.4)
        else: # A o nulo
            table_data.append(0.0)

        if self.object.go_41_p1 == 'D': 
            table_data.append(0.2*1.0)
        elif self.object.go_41_p1 == 'C':
            table_data.append(0.2*0.7)
        elif self.object.go_41_p1 == 'B':
            table_data.append(0.2*0.4)
        else: # A o nulo
            table_data.append(0.0)
  
        if self.object.go_41_p2 == 'D': 
            table_data.append(0.2*1.0)
        elif self.object.go_41_p2 == 'C':
            table_data.append(0.2*0.7)
        elif self.object.go_41_p2 == 'B':
            table_data.append(0.2*0.4)
        else: # A o nulo
            table_data.append(0.0)
       #go 4.2
        if self.object.go_42_act == 'E': 
            table_data.append(0.2*1.0)
        elif self.object.go_42_act == 'D':
            table_data.append(0.2*0.8)
        elif self.object.go_42_act == 'C':
            table_data.append(0.2*0.5)
        elif self.object.go_42_act == 'B':
            table_data.append(0.2*0.2)
        else: # A o nulo
            table_data.append(0.0)

        if self.object.go_42_p1 == 'E': 
            table_data.append(0.2*1.0)
        elif self.object.go_42_p1 == 'D':
            table_data.append(0.2*0.8)
        elif self.object.go_42_p1 == 'C':
            table_data.append(0.2*0.5)
        elif self.object.go_42_p1 == 'B':
            table_data.append(0.2*0.2)
        else: # A o nulo
            table_data.append(0.0)
  
        if self.object.go_42_p2 == 'E': 
            table_data.append(0.2*1.0)
        elif self.object.go_42_p2 == 'D':
            table_data.append(0.2*0.8)
        elif self.object.go_42_p2 == 'C':
            table_data.append(0.2*0.5)
        elif self.object.go_42_p2 == 'B':
            table_data.append(0.2*0.2)
        else: # A o nulo
            table_data.append(0.0)
       #go 4.3
        if self.object.go_43_act == 'E': 
            table_data.append(0.2*1.0)
        elif self.object.go_43_act == 'D':
            table_data.append(0.2*0.8)
        elif self.object.go_43_act == 'C':
            table_data.append(0.2*0.5)
        elif self.object.go_43_act == 'B':
            table_data.append(0.2*0.2)
        else: # A o nulo
            table_data.append(0.0)

        if self.object.go_43_p1 == 'E': 
            table_data.append(0.2*1.0)
        elif self.object.go_43_p1 == 'D':
            table_data.append(0.2*0.8)
        elif self.object.go_43_p1 == 'C':
            table_data.append(0.2*0.5)
        elif self.object.go_43_p1 == 'B':
            table_data.append(0.2*0.2)
        else: # A o nulo
            table_data.append(0.0)
  
        if self.object.go_43_p2 == 'E': 
            table_data.append(0.2*1.0)
        elif self.object.go_43_p2 == 'D':
            table_data.append(0.2*0.8)
        elif self.object.go_43_p2 == 'C':
            table_data.append(0.2*0.5)
        elif self.object.go_43_p2 == 'B':
            table_data.append(0.2*0.2)
        else: # A o nulo
            table_data.append(0.0)
        #go 4.4
        if self.object.go_44_act == 'D': 
            table_data.append(0.2*1.0)
        elif self.object.go_44_act == 'C':
            table_data.append(0.2*0.7)
        elif self.object.go_44_act == 'B':
            table_data.append(0.2*0.3)
        else: # A o nulo
            table_data.append(0.0)

        if self.object.go_44_p1 == 'D': 
            table_data.append(0.2*1.0)
        elif self.object.go_44_p1 == 'C':
            table_data.append(0.2*0.7)
        elif self.object.go_44_p1 == 'B':
            table_data.append(0.2*0.3)
        else: # A o nulo
            table_data.append(0.0)
  
        if self.object.go_44_p2 == 'D': 
            table_data.append(0.2*1.0)
        elif self.object.go_44_p2 == 'C':
            table_data.append(0.2*0.7)
        elif self.object.go_44_p2 == 'B':
            table_data.append(0.2*0.3)
        else: # A o nulo
            table_data.append(0.0)
        #go 4.5
        if self.object.go_45_act == 'D': 
            table_data.append(0.2*1.0)
        elif self.object.go_45_act == 'C':
            table_data.append(0.2*0.5)
        elif self.object.go_45_act == 'B':
            table_data.append(0.2*0.3)
        else: # A o nulo
            table_data.append(0.0)

        if self.object.go_45_p1 == 'D': 
            table_data.append(0.2*1.0)
        elif self.object.go_45_p1 == 'C':
            table_data.append(0.2*0.5)
        elif self.object.go_45_p1 == 'B':
            table_data.append(0.2*0.3)
        else: # A o nulo
            table_data.append(0.0)
  
        if self.object.go_45_p2 == 'D': 
            table_data.append(0.2*1.0)
        elif self.object.go_45_p2 == 'C':
            table_data.append(0.2*0.5)
        elif self.object.go_45_p2 == 'B':
            table_data.append(0.2*0.3)
        else: # A o nulo
            table_data.append(0.0)
       #go 5.1
        if self.object.go_51_act == 'E': 
            table_data.append(0.4*1.0)
        elif self.object.go_51_act == 'D':
            table_data.append(0.4*0.7)
        elif self.object.go_51_act == 'C':
            table_data.append(0.4*0.3)
        elif self.object.go_51_act == 'B':
            table_data.append(0.4*0.15)
        else: # A o nulo
            table_data.append(0.0)

        if self.object.go_51_p1 == 'E': 
            table_data.append(0.4*1.0)
        elif self.object.go_51_p1 == 'D':
            table_data.append(0.4*0.7)
        elif self.object.go_51_p1 == 'C':
            table_data.append(0.4*0.3)
        elif self.object.go_51_p1 == 'B':
            table_data.append(0.4*0.15)
        else: # A o nulo
            table_data.append(0.0)
  
        if self.object.go_51_p2 == 'E': 
            table_data.append(0.4*1.0)
        elif self.object.go_51_p2 == 'D':
            table_data.append(0.4*0.7)
        elif self.object.go_51_p2 == 'C':
            table_data.append(0.4*0.3)
        elif self.object.go_51_p2 == 'B':
            table_data.append(0.4*0.15)
        else: # A o nulo
            table_data.append(0.0)
        #go 5.2
        if self.object.go_52_act == 'D': 
            table_data.append(0.6*1.0)
        elif self.object.go_52_act == 'C':
            table_data.append(0.6*0.7)
        elif self.object.go_52_act == 'B':
            table_data.append(0.6*0.3)
        else: # A o nulo
            table_data.append(0.0)

        if self.object.go_52_p1 == 'D': 
            table_data.append(0.6*1.0)
        elif self.object.go_52_p1 == 'C':
            table_data.append(0.6*0.7)
        elif self.object.go_52_p1 == 'B':
            table_data.append(0.6*0.3)
        else: # A o nulo
            table_data.append(0.0)
  
        if self.object.go_52_p2 == 'D': 
            table_data.append(0.6*1.0)
        elif self.object.go_52_p2 == 'C':
            table_data.append(0.6*0.7)
        elif self.object.go_52_p2 == 'B':
            table_data.append(0.6*0.3)
        else: # A o nulo
            table_data.append(0.0)

        return table_data

    def get_table_data_wam(self):
        table_data = [] #lista vacia para almacenar resultados 
        #############WAM#################
                #wam 1.1
        if self.object.wam_11_act == 'D': 
            table_data.append(0.35*1.0)
        elif self.object.wam_11_act == 'C':
            table_data.append(0.35*0.7)
        elif self.object.wam_11_act == 'B':
            table_data.append(0.35*0.5)
        else: # A o nulo
            table_data.append(0.0)

        if self.object.wam_11_p1 == 'D': 
            table_data.append(0.35*1.0)
        elif self.object.wam_11_p1 == 'C':
            table_data.append(0.35*0.7)
        elif self.object.wam_11_p1 == 'B':
            table_data.append(0.35*0.5)
        else: # A o nulo
            table_data.append(0.0)
  
        if self.object.wam_11_p2 == 'D': 
            table_data.append(0.35*1.0)
        elif self.object.wam_11_p2 == 'C':
            table_data.append(0.35*0.7)
        elif self.object.wam_11_p2 == 'B':
            table_data.append(0.35*0.5)
        else: # A o nulo
            table_data.append(0.0)
        #wam 1.2
        if self.object.wam_12_act == 'D': 
            table_data.append(0.3*1.0)
        elif self.object.wam_12_act == 'C':
            table_data.append(0.3*0.7)
        elif self.object.wam_12_act == 'B':
            table_data.append(0.3*0.3)
        else: # A o nulo
            table_data.append(0.0)

        if self.object.wam_12_p1 == 'D': 
            table_data.append(0.3*1.0)
        elif self.object.wam_12_p1 == 'C':
            table_data.append(0.3*0.7)
        elif self.object.wam_12_p1 == 'B':
            table_data.append(0.3*0.3)
        else: # A o nulo
            table_data.append(0.0)
  
        if self.object.wam_12_p2 == 'D': 
            table_data.append(0.3*1.0)
        elif self.object.wam_12_p2 == 'C':
            table_data.append(0.3*0.7)
        elif self.object.wam_12_p2 == 'B':
            table_data.append(0.3*0.3)
        else: # A o nulo
            table_data.append(0.0)
        #wam 1.3
        if self.object.wam_13_act == 'D': 
            table_data.append(0.35*1.0)
        elif self.object.wam_13_act == 'C':
            table_data.append(0.35*0.7)
        elif self.object.wam_13_act == 'B':
            table_data.append(0.35*0.2)
        else: # A o nulo
            table_data.append(0.0)

        if self.object.wam_13_p1 == 'D': 
            table_data.append(0.35*1.0)
        elif self.object.wam_13_p1 == 'C':
            table_data.append(0.35*0.7)
        elif self.object.wam_13_p1 == 'B':
            table_data.append(0.35*0.2)
        else: # A o nulo
            table_data.append(0.0)
  
        if self.object.wam_13_p2 == 'D': 
            table_data.append(0.35*1.0)
        elif self.object.wam_13_p2 == 'C':
            table_data.append(0.35*0.7)
        elif self.object.wam_13_p2 == 'B':
            table_data.append(0.35*0.2)
        else: # A o nulo
            table_data.append(0.0)
       #wam 2.1
        if self.object.wam_21_act == 'E': 
            table_data.append(0.45*1.0)
        elif self.object.wam_21_act == 'D':
            table_data.append(0.45*0.7)
        elif self.object.wam_21_act == 'C':
            table_data.append(0.45*0.5)
        elif self.object.wam_21_act == 'B':
            table_data.append(0.45*0.3)
        else: # A o nulo
            table_data.append(0.0)

        if self.object.wam_21_p1 == 'E': 
            table_data.append(0.45*1.0)
        elif self.object.wam_21_p1 == 'D':
            table_data.append(0.45*0.7)
        elif self.object.wam_21_p1 == 'C':
            table_data.append(0.45*0.5)
        elif self.object.wam_21_p1 == 'B':
            table_data.append(0.45*0.3)
        else: # A o nulo
            table_data.append(0.0)
  
        if self.object.wam_21_p2 == 'E': 
            table_data.append(0.45*1.0)
        elif self.object.wam_21_p2 == 'D':
            table_data.append(0.45*0.7)
        elif self.object.wam_21_p2 == 'C':
            table_data.append(0.45*0.5)
        elif self.object.wam_21_p2 == 'B':
            table_data.append(0.45*0.3)
        else: # A o nulo
            table_data.append(0.0)
       #wam 2.2
        if self.object.wam_22_act == 'E': 
            table_data.append(0.35*1.0)
        elif self.object.wam_22_act == 'D':
            table_data.append(0.35*0.7)
        elif self.object.wam_22_act == 'C':
            table_data.append(0.35*0.5)
        elif self.object.wam_22_act == 'B':
            table_data.append(0.35*0.3)
        else: # A o nulo
            table_data.append(0.0)

        if self.object.wam_22_p1 == 'E': 
            table_data.append(0.35*1.0)
        elif self.object.wam_22_p1 == 'D':
            table_data.append(0.35*0.7)
        elif self.object.wam_22_p1 == 'C':
            table_data.append(0.35*0.5)
        elif self.object.wam_22_p1 == 'B':
            table_data.append(0.35*0.3)
        else: # A o nulo
            table_data.append(0.0)
  
        if self.object.wam_22_p2 == 'E': 
            table_data.append(0.35*1.0)
        elif self.object.wam_22_p2 == 'D':
            table_data.append(0.35*0.7)
        elif self.object.wam_22_p2 == 'C':
            table_data.append(0.35*0.5)
        elif self.object.wam_22_p2 == 'B':
            table_data.append(0.35*0.3)
        else: # A o nulo
            table_data.append(0.0)
        #wam 2.3
        if self.object.wam_23_act == 'D': 
            table_data.append(0.2*1.0)
        elif self.object.wam_23_act == 'C':
            table_data.append(0.2*0.5)
        elif self.object.wam_23_act == 'B':
            table_data.append(0.2*0.3)
        else: # A o nulo
            table_data.append(0.0)

        if self.object.wam_23_p1 == 'D': 
            table_data.append(0.2*1.0)
        elif self.object.wam_23_p1 == 'C':
            table_data.append(0.2*0.5)
        elif self.object.wam_23_p1 == 'B':
            table_data.append(0.2*0.3)
        else: # A o nulo
            table_data.append(0.0)
  
        if self.object.wam_23_p2 == 'D': 
            table_data.append(0.2*1.0)
        elif self.object.wam_23_p2 == 'C':
            table_data.append(0.2*0.5)
        elif self.object.wam_23_p2 == 'B':
            table_data.append(0.2*0.3)
        else: # A o nulo
            table_data.append(0.0)
       #wam 3.1
        if self.object.wam_31_act == 'E': 
            table_data.append(0.14*1.0)
        elif self.object.wam_31_act == 'D':
            table_data.append(0.14*0.7)
        elif self.object.wam_31_act == 'C':
            table_data.append(0.14*0.4)
        elif self.object.wam_31_act == 'B':
            table_data.append(0.14*0.2)
        else: # A o nulo
            table_data.append(0.0)

        if self.object.wam_31_p1 == 'E': 
            table_data.append(0.14*1.0)
        elif self.object.wam_31_p1 == 'D':
            table_data.append(0.14*0.7)
        elif self.object.wam_31_p1 == 'C':
            table_data.append(0.14*0.4)
        elif self.object.wam_31_p1 == 'B':
            table_data.append(0.14*0.2)
        else: # A o nulo
            table_data.append(0.0)
  
        if self.object.wam_31_p2 == 'E': 
            table_data.append(0.14*1.0)
        elif self.object.wam_31_p2 == 'D':
            table_data.append(0.14*0.7)
        elif self.object.wam_31_p2 == 'C':
            table_data.append(0.14*0.4)
        elif self.object.wam_31_p2 == 'B':
            table_data.append(0.14*0.2)
        else: # A o nulo
            table_data.append(0.0)
       #wam 3.2
        if self.object.wam_32_act == 'E': 
            table_data.append(0.14*1.0)
        elif self.object.wam_32_act == 'D':
            table_data.append(0.14*0.7)
        elif self.object.wam_32_act == 'C':
            table_data.append(0.14*0.4)
        elif self.object.wam_32_act == 'B':
            table_data.append(0.14*0.2)
        else: # A o nulo
            table_data.append(0.0)

        if self.object.wam_32_p1 == 'E': 
            table_data.append(0.14*1.0)
        elif self.object.wam_32_p1 == 'D':
            table_data.append(0.14*0.7)
        elif self.object.wam_32_p1 == 'C':
            table_data.append(0.14*0.4)
        elif self.object.wam_32_p1 == 'B':
            table_data.append(0.14*0.2)
        else: # A o nulo
            table_data.append(0.0)
  
        if self.object.wam_32_p2 == 'E': 
            table_data.append(0.14*1.0)
        elif self.object.wam_32_p2 == 'D':
            table_data.append(0.14*0.7)
        elif self.object.wam_32_p2 == 'C':
            table_data.append(0.14*0.4)
        elif self.object.wam_32_p2 == 'B':
            table_data.append(0.14*0.2)
        else: # A o nulo
            table_data.append(0.0)
       #wam 3.3
        if self.object.wam_33_act == 'E': 
            table_data.append(0.14*1.0)
        elif self.object.wam_33_act == 'D':
            table_data.append(0.14*0.7)
        elif self.object.wam_33_act == 'C':
            table_data.append(0.14*0.5)
        elif self.object.wam_33_act == 'B':
            table_data.append(0.14*0.3)
        else: # A o nulo
            table_data.append(0.0)

        if self.object.wam_33_p1 == 'E': 
            table_data.append(0.14*1.0)
        elif self.object.wam_33_p1 == 'D':
            table_data.append(0.14*0.7)
        elif self.object.wam_33_p1 == 'C':
            table_data.append(0.14*0.5)
        elif self.object.wam_33_p1 == 'B':
            table_data.append(0.14*0.3)
        else: # A o nulo
            table_data.append(0.0)
  
        if self.object.wam_33_p2 == 'E': 
            table_data.append(0.14*1.0)
        elif self.object.wam_33_p2 == 'D':
            table_data.append(0.14*0.7)
        elif self.object.wam_33_p2 == 'C':
            table_data.append(0.14*0.5)
        elif self.object.wam_33_p2 == 'B':
            table_data.append(0.14*0.3)
        else: # A o nulo
            table_data.append(0.0)
       #wam 3.4
        if self.object.wam_34_act == 'E': 
            table_data.append(0.14*1.0)
        elif self.object.wam_34_act == 'D':
            table_data.append(0.14*0.7)
        elif self.object.wam_34_act == 'C':
            table_data.append(0.14*0.5)
        elif self.object.wam_34_act == 'B':
            table_data.append(0.14*0.3)
        else: # A o nulo
            table_data.append(0.0)

        if self.object.wam_34_p1 == 'E': 
            table_data.append(0.14*1.0)
        elif self.object.wam_34_p1 == 'D':
            table_data.append(0.14*0.7)
        elif self.object.wam_34_p1 == 'C':
            table_data.append(0.14*0.5)
        elif self.object.wam_34_p1 == 'B':
            table_data.append(0.14*0.3)
        else: # A o nulo
            table_data.append(0.0)
  
        if self.object.wam_34_p2 == 'E': 
            table_data.append(0.14*1.0)
        elif self.object.wam_34_p2 == 'D':
            table_data.append(0.14*0.7)
        elif self.object.wam_34_p2 == 'C':
            table_data.append(0.14*0.5)
        elif self.object.wam_34_p2 == 'B':
            table_data.append(0.14*0.3)
        else: # A o nulo
            table_data.append(0.0)
       #wam 3.5
        if self.object.wam_35_act == 'E': 
            table_data.append(0.14*1.0)
        elif self.object.wam_35_act == 'D':
            table_data.append(0.14*0.7)
        elif self.object.wam_35_act == 'C':
            table_data.append(0.14*0.5)
        elif self.object.wam_35_act == 'B':
            table_data.append(0.14*0.3)
        else: # A o nulo
            table_data.append(0.0)

        if self.object.wam_35_p1 == 'E': 
            table_data.append(0.14*1.0)
        elif self.object.wam_35_p1 == 'D':
            table_data.append(0.14*0.7)
        elif self.object.wam_35_p1 == 'C':
            table_data.append(0.14*0.5)
        elif self.object.wam_35_p1 == 'B':
            table_data.append(0.14*0.3)
        else: # A o nulo
            table_data.append(0.0)
  
        if self.object.wam_35_p2 == 'E': 
            table_data.append(0.14*1.0)
        elif self.object.wam_35_p2 == 'D':
            table_data.append(0.14*0.7)
        elif self.object.wam_35_p2 == 'C':
            table_data.append(0.14*0.5)
        elif self.object.wam_35_p2 == 'B':
            table_data.append(0.14*0.3)
        else: # A o nulo
            table_data.append(0.0)
       #wam 3.6
        if self.object.wam_36_act == 'E': 
            table_data.append(0.14*1.0)
        elif self.object.wam_36_act == 'D':
            table_data.append(0.14*0.7)
        elif self.object.wam_36_act == 'C':
            table_data.append(0.14*0.4)
        elif self.object.wam_36_act == 'B':
            table_data.append(0.14*0.2)
        else: # A o nulo
            table_data.append(0.0)

        if self.object.wam_36_p1 == 'E': 
            table_data.append(0.14*1.0)
        elif self.object.wam_36_p1 == 'D':
            table_data.append(0.14*0.7)
        elif self.object.wam_36_p1 == 'C':
            table_data.append(0.14*0.4)
        elif self.object.wam_36_p1 == 'B':
            table_data.append(0.14*0.2)
        else: # A o nulo
            table_data.append(0.0)
  
        if self.object.wam_36_p2 == 'E': 
            table_data.append(0.14*1.0)
        elif self.object.wam_36_p2 == 'D':
            table_data.append(0.14*0.7)
        elif self.object.wam_36_p2 == 'C':
            table_data.append(0.14*0.4)
        elif self.object.wam_36_p2 == 'B':
            table_data.append(0.14*0.2)
        else: # A o nulo
            table_data.append(0.0)
       #wam 3.7
        if self.object.wam_37_act == 'E': 
            table_data.append(0.15*1.0)
        elif self.object.wam_37_act == 'D':
            table_data.append(0.15*0.7)
        elif self.object.wam_37_act == 'C':
            table_data.append(0.15*0.5)
        elif self.object.wam_37_act == 'B':
            table_data.append(0.15*0.3)
        else: # A o nulo
            table_data.append(0.0)

        if self.object.wam_37_p1 == 'E': 
            table_data.append(0.15*1.0)
        elif self.object.wam_37_p1 == 'D':
            table_data.append(0.15*0.7)
        elif self.object.wam_37_p1 == 'C':
            table_data.append(0.15*0.5)
        elif self.object.wam_37_p1 == 'B':
            table_data.append(0.15*0.3)
        else: # A o nulo
            table_data.append(0.0)
  
        if self.object.wam_37_p2 == 'E': 
            table_data.append(0.15*1.0)
        elif self.object.wam_37_p2 == 'D':
            table_data.append(0.15*0.7)
        elif self.object.wam_37_p2 == 'C':
            table_data.append(0.15*0.5)
        elif self.object.wam_37_p2 == 'B':
            table_data.append(0.15*0.3)
        else: # A o nulo
            table_data.append(0.0)
       #wam 4.1
        if self.object.wam_41_act == 'E': 
            table_data.append(0.25*1.0)
        elif self.object.wam_41_act == 'D':
            table_data.append(0.25*0.7)
        elif self.object.wam_41_act == 'C':
            table_data.append(0.25*0.4)
        elif self.object.wam_41_act == 'B':
            table_data.append(0.25*0.2)
        else: # A o nulo
            table_data.append(0.0)

        if self.object.wam_41_p1 == 'E': 
            table_data.append(0.25*1.0)
        elif self.object.wam_41_p1 == 'D':
            table_data.append(0.25*0.7)
        elif self.object.wam_41_p1 == 'C':
            table_data.append(0.25*0.4)
        elif self.object.wam_41_p1 == 'B':
            table_data.append(0.25*0.2)
        else: # A o nulo
            table_data.append(0.0)
  
        if self.object.wam_41_p2 == 'E': 
            table_data.append(0.25*1.0)
        elif self.object.wam_41_p2 == 'D':
            table_data.append(0.25*0.7)
        elif self.object.wam_41_p2 == 'C':
            table_data.append(0.25*0.4)
        elif self.object.wam_41_p2 == 'B':
            table_data.append(0.25*0.2)
        else: # A o nulo
            table_data.append(0.0)
       #wam 4.2
        if self.object.wam_42_act == 'E': 
            table_data.append(0.25*1.0)
        elif self.object.wam_42_act == 'D':
            table_data.append(0.25*0.7)
        elif self.object.wam_42_act == 'C':
            table_data.append(0.25*0.4)
        elif self.object.wam_42_act == 'B':
            table_data.append(0.25*0.2)
        else: # A o nulo
            table_data.append(0.0)

        if self.object.wam_42_p1 == 'E': 
            table_data.append(0.25*1.0)
        elif self.object.wam_42_p1 == 'D':
            table_data.append(0.25*0.7)
        elif self.object.wam_42_p1 == 'C':
            table_data.append(0.25*0.4)
        elif self.object.wam_42_p1 == 'B':
            table_data.append(0.25*0.2)
        else: # A o nulo
            table_data.append(0.0)
  
        if self.object.wam_42_p2 == 'E': 
            table_data.append(0.25*1.0)
        elif self.object.wam_42_p2 == 'D':
            table_data.append(0.25*0.7)
        elif self.object.wam_42_p2 == 'C':
            table_data.append(0.25*0.4)
        elif self.object.wam_42_p2 == 'B':
            table_data.append(0.25*0.2)
        else: # A o nulo
            table_data.append(0.0)
       #wam 4.3
        if self.object.wam_43_act == 'E': 
            table_data.append(0.25*1.0)
        elif self.object.wam_43_act == 'D':
            table_data.append(0.25*0.7)
        elif self.object.wam_43_act == 'C':
            table_data.append(0.25*0.4)
        elif self.object.wam_43_act == 'B':
            table_data.append(0.25*0.2)
        else: # A o nulo
            table_data.append(0.0)

        if self.object.wam_43_p1 == 'E': 
            table_data.append(0.25*1.0)
        elif self.object.wam_43_p1 == 'D':
            table_data.append(0.25*0.7)
        elif self.object.wam_43_p1 == 'C':
            table_data.append(0.25*0.4)
        elif self.object.wam_43_p1 == 'B':
            table_data.append(0.25*0.2)
        else: # A o nulo
            table_data.append(0.0)
  
        if self.object.wam_43_p2 == 'E': 
            table_data.append(0.25*1.0)
        elif self.object.wam_43_p2 == 'D':
            table_data.append(0.25*0.7)
        elif self.object.wam_43_p2 == 'C':
            table_data.append(0.25*0.4)
        elif self.object.wam_43_p2 == 'B':
            table_data.append(0.25*0.2)
        else: # A o nulo
            table_data.append(0.0)
       #wam 4.4
        if self.object.wam_44_act == 'E': 
            table_data.append(0.25*1.0)
        elif self.object.wam_44_act == 'D':
            table_data.append(0.25*0.7)
        elif self.object.wam_44_act == 'C':
            table_data.append(0.25*0.4)
        elif self.object.wam_44_act == 'B':
            table_data.append(0.25*0.2)
        else: # A o nulo
            table_data.append(0.0)

        if self.object.wam_44_p1 == 'E': 
            table_data.append(0.25*1.0)
        elif self.object.wam_44_p1 == 'D':
            table_data.append(0.25*0.7)
        elif self.object.wam_44_p1 == 'C':
            table_data.append(0.25*0.4)
        elif self.object.wam_44_p1 == 'B':
            table_data.append(0.25*0.2)
        else: # A o nulo
            table_data.append(0.0)
  
        if self.object.wam_44_p2 == 'E': 
            table_data.append(0.25*1.0)
        elif self.object.wam_44_p2 == 'D':
            table_data.append(0.25*0.7)
        elif self.object.wam_44_p2 == 'C':
            table_data.append(0.25*0.4)
        elif self.object.wam_44_p2 == 'B':
            table_data.append(0.25*0.2)
        else: # A o nulo
            table_data.append(0.0)
       #wam 5.1
        if self.object.wam_51_act == 'E': 
            table_data.append(0.5*1.0)
        elif self.object.wam_51_act == 'D':
            table_data.append(0.5*0.7)
        elif self.object.wam_51_act == 'C':
            table_data.append(0.5*0.3)
        elif self.object.wam_51_act == 'B':
            table_data.append(0.5*0.1)
        else: # A o nulo
            table_data.append(0.0)

        if self.object.wam_51_p1 == 'E': 
            table_data.append(0.5*1.0)
        elif self.object.wam_51_p1 == 'D':
            table_data.append(0.5*0.7)
        elif self.object.wam_51_p1 == 'C':
            table_data.append(0.5*0.3)
        elif self.object.wam_51_p1 == 'B':
            table_data.append(0.5*0.1)
        else: # A o nulo
            table_data.append(0.0)
  
        if self.object.wam_51_p2 == 'E': 
            table_data.append(0.5*1.0)
        elif self.object.wam_51_p2 == 'D':
            table_data.append(0.5*0.7)
        elif self.object.wam_51_p2 == 'C':
            table_data.append(0.5*0.3)
        elif self.object.wam_51_p2 == 'B':
            table_data.append(0.5*0.1)
        else: # A o nulo
            table_data.append(0.0)
       #wam 5.2
        if self.object.wam_52_act == 'E': 
            table_data.append(0.5*1.0)
        elif self.object.wam_52_act == 'D':
            table_data.append(0.5*0.7)
        elif self.object.wam_52_act == 'C':
            table_data.append(0.5*0.3)
        elif self.object.wam_52_act == 'B':
            table_data.append(0.5*0.1)
        else: # A o nulo
            table_data.append(0.0)

        if self.object.wam_52_p1 == 'E': 
            table_data.append(0.5*1.0)
        elif self.object.wam_52_p1 == 'D':
            table_data.append(0.5*0.7)
        elif self.object.wam_52_p1 == 'C':
            table_data.append(0.5*0.3)
        elif self.object.wam_52_p1 == 'B':
            table_data.append(0.5*0.1)
        else: # A o nulo
            table_data.append(0.0)
  
        if self.object.wam_52_p2 == 'E': 
            table_data.append(0.5*1.0)
        elif self.object.wam_52_p2 == 'D':
            table_data.append(0.5*0.7)
        elif self.object.wam_52_p2 == 'C':
            table_data.append(0.5*0.3)
        elif self.object.wam_52_p2 == 'B':
            table_data.append(0.5*0.1)
        else: # A o nulo
            table_data.append(0.0)

        return table_data

    def get_table_data_tech(self):
        table_data = [] #lista vacia para almacenar resultados 
        #############TECH#################
                #tech 1.1
        if self.object.tech_11_act == 'D': 
            table_data.append(0.2*1.0)
        elif self.object.tech_11_act == 'C':
            table_data.append(0.2*0.7)
        elif self.object.tech_11_act == 'B':
            table_data.append(0.2*0.5)
        else: # A o nulo
            table_data.append(0.0)

        if self.object.tech_11_p1 == 'D': 
            table_data.append(0.2*1.0)
        elif self.object.tech_11_p1 == 'C':
            table_data.append(0.2*0.7)
        elif self.object.tech_11_p1 == 'B':
            table_data.append(0.2*0.5)
        else: # A o nulo
            table_data.append(0.0)
  
        if self.object.tech_11_p2 == 'D': 
            table_data.append(0.2*1.0)
        elif self.object.tech_11_p2 == 'C':
            table_data.append(0.2*0.7)
        elif self.object.tech_11_p2 == 'B':
            table_data.append(0.2*0.5)
        else: # A o nulo
            table_data.append(0.0)
        #tech 1.2
        if self.object.tech_12_act == 'D': 
            table_data.append(0.2*1.0)
        elif self.object.tech_12_act == 'C':
            table_data.append(0.2*0.7)
        elif self.object.tech_12_act == 'B':
            table_data.append(0.2*0.5)
        else: # A o nulo
            table_data.append(0.0)

        if self.object.tech_12_p1 == 'D': 
            table_data.append(0.2*1.0)
        elif self.object.tech_12_p1 == 'C':
            table_data.append(0.2*0.7)
        elif self.object.tech_12_p1 == 'B':
            table_data.append(0.2*0.5)
        else: # A o nulo
            table_data.append(0.0)
  
        if self.object.tech_12_p2 == 'D': 
            table_data.append(0.2*1.0)
        elif self.object.tech_12_p2 == 'C':
            table_data.append(0.2*0.7)
        elif self.object.tech_12_p2 == 'B':
            table_data.append(0.2*0.5)
        else: # A o nulo
            table_data.append(0.0)
       #tech 1.3
        if self.object.tech_13_act == 'E': 
            table_data.append(0.2*1.0)
        elif self.object.tech_13_act == 'D':
            table_data.append(0.2*0.7)
        elif self.object.tech_13_act == 'C':
            table_data.append(0.2*0.5)
        elif self.object.tech_13_act == 'B':
            table_data.append(0.2*0.3)
        else: # A o nulo
            table_data.append(0.0)

        if self.object.tech_13_p1 == 'E': 
            table_data.append(0.2*1.0)
        elif self.object.tech_13_p1 == 'D':
            table_data.append(0.2*0.7)
        elif self.object.tech_13_p1 == 'C':
            table_data.append(0.2*0.5)
        elif self.object.tech_13_p1 == 'B':
            table_data.append(0.2*0.3)
        else: # A o nulo
            table_data.append(0.0)
  
        if self.object.tech_13_p2 == 'E': 
            table_data.append(0.2*1.0)
        elif self.object.tech_13_p2 == 'D':
            table_data.append(0.2*0.7)
        elif self.object.tech_13_p2 == 'C':
            table_data.append(0.2*0.5)
        elif self.object.tech_13_p2 == 'B':
            table_data.append(0.2*0.3)
        else: # A o nulo
            table_data.append(0.0)
        #tech 1.4
        if self.object.tech_14_act == 'D': 
            table_data.append(0.2*1.0)
        elif self.object.tech_14_act == 'C':
            table_data.append(0.2*0.9)
        elif self.object.tech_14_act == 'B':
            table_data.append(0.2*0.5)
        else: # A o nulo
            table_data.append(0.0)

        if self.object.tech_14_p1 == 'D': 
            table_data.append(0.2*1.0)
        elif self.object.tech_14_p1 == 'C':
            table_data.append(0.2*0.9)
        elif self.object.tech_14_p1 == 'B':
            table_data.append(0.2*0.5)
        else: # A o nulo
            table_data.append(0.0)
  
        if self.object.tech_14_p2 == 'D': 
            table_data.append(0.2*1.0)
        elif self.object.tech_14_p2 == 'C':
            table_data.append(0.2*0.9)
        elif self.object.tech_14_p2 == 'B':
            table_data.append(0.2*0.5)
        else: # A o nulo
            table_data.append(0.0)
       #tech 1.5
        if self.object.tech_15_act == 'E': 
            table_data.append(0.2*1.0)
        elif self.object.tech_15_act == 'D':
            table_data.append(0.2*0.7)
        elif self.object.tech_15_act == 'C':
            table_data.append(0.2*0.5)
        elif self.object.tech_15_act == 'B':
            table_data.append(0.2*0.3)
        else: # A o nulo
            table_data.append(0.0)

        if self.object.tech_15_p1 == 'E': 
            table_data.append(0.2*1.0)
        elif self.object.tech_15_p1 == 'D':
            table_data.append(0.2*0.7)
        elif self.object.tech_15_p1 == 'C':
            table_data.append(0.2*0.5)
        elif self.object.tech_15_p1 == 'B':
            table_data.append(0.2*0.3)
        else: # A o nulo
            table_data.append(0.0)
  
        if self.object.tech_15_p2 == 'E': 
            table_data.append(0.2*1.0)
        elif self.object.tech_15_p2 == 'D':
            table_data.append(0.2*0.7)
        elif self.object.tech_15_p2 == 'C':
            table_data.append(0.2*0.5)
        elif self.object.tech_15_p2 == 'B':
            table_data.append(0.2*0.3)
        else: # A o nulo
            table_data.append(0.0)
        #tech 2.1
        if self.object.tech_21_act == 'D': 
            table_data.append(0.16*1.0)
        elif self.object.tech_21_act == 'C':
            table_data.append(0.16*0.7)
        elif self.object.tech_21_act == 'B':
            table_data.append(0.16*0.5)
        else: # A o nulo
            table_data.append(0.0)

        if self.object.tech_21_p1 == 'D': 
            table_data.append(0.16*1.0)
        elif self.object.tech_21_p1 == 'C':
            table_data.append(0.16*0.7)
        elif self.object.tech_21_p1 == 'B':
            table_data.append(0.16*0.5)
        else: # A o nulo
            table_data.append(0.0)
  
        if self.object.tech_21_p2 == 'D': 
            table_data.append(0.16*1.0)
        elif self.object.tech_21_p2 == 'C':
            table_data.append(0.16*0.7)
        elif self.object.tech_21_p2 == 'B':
            table_data.append(0.16*0.5)
        else: # A o nulo
            table_data.append(0.0)
       #tech 2.2
        if self.object.tech_22_act == 'E': 
            table_data.append(0.16*1.0)
        elif self.object.tech_22_act == 'D':
            table_data.append(0.16*0.7)
        elif self.object.tech_22_act == 'C':
            table_data.append(0.16*0.5)
        elif self.object.tech_22_act == 'B':
            table_data.append(0.16*0.3)
        else: # A o nulo
            table_data.append(0.0)

        if self.object.tech_22_p1 == 'E': 
            table_data.append(0.16*1.0)
        elif self.object.tech_22_p1 == 'D':
            table_data.append(0.16*0.7)
        elif self.object.tech_22_p1 == 'C':
            table_data.append(0.16*0.5)
        elif self.object.tech_22_p1 == 'B':
            table_data.append(0.16*0.3)
        else: # A o nulo
            table_data.append(0.0)
  
        if self.object.tech_22_p2 == 'E': 
            table_data.append(0.16*1.0)
        elif self.object.tech_22_p2 == 'D':
            table_data.append(0.16*0.7)
        elif self.object.tech_22_p2 == 'C':
            table_data.append(0.16*0.5)
        elif self.object.tech_22_p2 == 'B':
            table_data.append(0.16*0.3)
        else: # A o nulo
            table_data.append(0.0)
        #tech 2.3
        if self.object.tech_23_act == 'D': 
            table_data.append(0.16*1.0)
        elif self.object.tech_23_act == 'C':
            table_data.append(0.16*0.7)
        elif self.object.tech_23_act == 'B':
            table_data.append(0.16*0.5)
        else: # A o nulo
            table_data.append(0.0)

        if self.object.tech_23_p1 == 'D': 
            table_data.append(0.16*1.0)
        elif self.object.tech_23_p1 == 'C':
            table_data.append(0.16*0.7)
        elif self.object.tech_23_p1 == 'B':
            table_data.append(0.16*0.5)
        else: # A o nulo
            table_data.append(0.0)
  
        if self.object.tech_23_p2 == 'D': 
            table_data.append(0.16*1.0)
        elif self.object.tech_23_p2 == 'C':
            table_data.append(0.16*0.7)
        elif self.object.tech_23_p2 == 'B':
            table_data.append(0.16*0.5)
        else: # A o nulo
            table_data.append(0.0)
        #tech 2.4
        if self.object.tech_24_act == 'D': 
            table_data.append(0.12*1.0)
        elif self.object.tech_24_act == 'C':
            table_data.append(0.12*0.7)
        elif self.object.tech_24_act == 'B':
            table_data.append(0.12*0.5)
        else: # A o nulo
            table_data.append(0.0)

        if self.object.tech_24_p1 == 'D': 
            table_data.append(0.12*1.0)
        elif self.object.tech_24_p1 == 'C':
            table_data.append(0.12*0.7)
        elif self.object.tech_24_p1 == 'B':
            table_data.append(0.12*0.5)
        else: # A o nulo
            table_data.append(0.0)
  
        if self.object.tech_24_p2 == 'D': 
            table_data.append(0.12*1.0)
        elif self.object.tech_24_p2 == 'C':
            table_data.append(0.12*0.7)
        elif self.object.tech_24_p2 == 'B':
            table_data.append(0.12*0.5)
        else: # A o nulo
            table_data.append(0.0)
       #tech 2.5
        if self.object.tech_25_act == 'E': 
            table_data.append(0.16*1.0)
        elif self.object.tech_25_act == 'D':
            table_data.append(0.16*0.7)
        elif self.object.tech_25_act == 'C':
            table_data.append(0.16*0.5)
        elif self.object.tech_25_act == 'B':
            table_data.append(0.16*0.3)
        else: # A o nulo
            table_data.append(0.0)

        if self.object.tech_25_p1 == 'E': 
            table_data.append(0.16*1.0)
        elif self.object.tech_25_p1 == 'D':
            table_data.append(0.16*0.7)
        elif self.object.tech_25_p1 == 'C':
            table_data.append(0.16*0.5)
        elif self.object.tech_25_p1 == 'B':
            table_data.append(0.16*0.3)
        else: # A o nulo
            table_data.append(0.0)
  
        if self.object.tech_25_p2 == 'E': 
            table_data.append(0.16*1.0)
        elif self.object.tech_25_p2 == 'D':
            table_data.append(0.16*0.7)
        elif self.object.tech_25_p2 == 'C':
            table_data.append(0.16*0.5)
        elif self.object.tech_25_p2 == 'B':
            table_data.append(0.16*0.3)
        else: # A o nulo
            table_data.append(0.0)
       #tech 2.6
        if self.object.tech_26_act == 'E': 
            table_data.append(0.12*1.0)
        elif self.object.tech_26_act == 'D':
            table_data.append(0.12*0.7)
        elif self.object.tech_26_act == 'C':
            table_data.append(0.12*0.3)
        elif self.object.tech_26_act == 'B':
            table_data.append(0.12*0.0)
        else: # A o nulo
            table_data.append(0.0)

        if self.object.tech_26_p1 == 'E': 
            table_data.append(0.12*1.0)
        elif self.object.tech_26_p1 == 'D':
            table_data.append(0.12*0.7)
        elif self.object.tech_26_p1 == 'C':
            table_data.append(0.12*0.3)
        elif self.object.tech_26_p1 == 'B':
            table_data.append(0.12*0.0)
        else: # A o nulo
            table_data.append(0.0)
  
        if self.object.tech_26_p2 == 'E': 
            table_data.append(0.12*1.0)
        elif self.object.tech_26_p2 == 'D':
            table_data.append(0.12*0.7)
        elif self.object.tech_26_p2 == 'C':
            table_data.append(0.12*0.3)
        elif self.object.tech_26_p2 == 'B':
            table_data.append(0.12*0.0)
        else: # A o nulo
            table_data.append(0.0)
       #tech 2.7
        if self.object.tech_27_act == 'E': 
            table_data.append(0.12*1.0)
        elif self.object.tech_27_act == 'D':
            table_data.append(0.12*0.7)
        elif self.object.tech_27_act == 'C':
            table_data.append(0.12*0.5)
        elif self.object.tech_27_act == 'B':
            table_data.append(0.12*0.3)
        else: # A o nulo
            table_data.append(0.0)

        if self.object.tech_27_p1 == 'E': 
            table_data.append(0.12*1.0)
        elif self.object.tech_27_p1 == 'D':
            table_data.append(0.12*0.7)
        elif self.object.tech_27_p1 == 'C':
            table_data.append(0.12*0.5)
        elif self.object.tech_27_p1 == 'B':
            table_data.append(0.12*0.3)
        else: # A o nulo
            table_data.append(0.0)
  
        if self.object.tech_27_p2 == 'E': 
            table_data.append(0.12*1.0)
        elif self.object.tech_27_p2 == 'D':
            table_data.append(0.12*0.7)
        elif self.object.tech_27_p2 == 'C':
            table_data.append(0.12*0.5)
        elif self.object.tech_27_p2 == 'B':
            table_data.append(0.12*0.3)
        else: # A o nulo
            table_data.append(0.0)
       #tech 3.1
        if self.object.tech_31_act == 'E': 
            table_data.append(0.17*1.0)
        elif self.object.tech_31_act == 'D':
            table_data.append(0.17*0.7)
        elif self.object.tech_31_act == 'C':
            table_data.append(0.17*0.5)
        elif self.object.tech_31_act == 'B':
            table_data.append(0.17*0.3)
        else: # A o nulo
            table_data.append(0.0)

        if self.object.tech_31_p1 == 'E': 
            table_data.append(0.17*1.0)
        elif self.object.tech_31_p1 == 'D':
            table_data.append(0.17*0.7)
        elif self.object.tech_31_p1 == 'C':
            table_data.append(0.17*0.5)
        elif self.object.tech_31_p1 == 'B':
            table_data.append(0.17*0.3)
        else: # A o nulo
            table_data.append(0.0)
  
        if self.object.tech_31_p2 == 'E': 
            table_data.append(0.17*1.0)
        elif self.object.tech_31_p2 == 'D':
            table_data.append(0.17*0.7)
        elif self.object.tech_31_p2 == 'C':
            table_data.append(0.17*0.5)
        elif self.object.tech_31_p2 == 'B':
            table_data.append(0.17*0.3)
        else: # A o nulo
            table_data.append(0.0)
       #tech 3.2
        if self.object.tech_32_act == 'E': 
            table_data.append(0.17*1.0)
        elif self.object.tech_32_act == 'D':
            table_data.append(0.17*0.7)
        elif self.object.tech_32_act == 'C':
            table_data.append(0.17*0.5)
        elif self.object.tech_32_act == 'B':
            table_data.append(0.17*0.3)
        else: # A o nulo
            table_data.append(0.0)

        if self.object.tech_32_p1 == 'E': 
            table_data.append(0.17*1.0)
        elif self.object.tech_32_p1 == 'D':
            table_data.append(0.17*0.7)
        elif self.object.tech_32_p1 == 'C':
            table_data.append(0.17*0.5)
        elif self.object.tech_32_p1 == 'B':
            table_data.append(0.17*0.3)
        else: # A o nulo
            table_data.append(0.0)
  
        if self.object.tech_32_p2 == 'E': 
            table_data.append(0.17*1.0)
        elif self.object.tech_32_p2 == 'D':
            table_data.append(0.17*0.7)
        elif self.object.tech_32_p2 == 'C':
            table_data.append(0.17*0.5)
        elif self.object.tech_32_p2 == 'B':
            table_data.append(0.17*0.3)
        else: # A o nulo
            table_data.append(0.0)
       #tech 3.3
        if self.object.tech_33_act == 'E': 
            table_data.append(0.17*1.0)
        elif self.object.tech_33_act == 'D':
            table_data.append(0.17*0.7)
        elif self.object.tech_33_act == 'C':
            table_data.append(0.17*0.5)
        elif self.object.tech_33_act == 'B':
            table_data.append(0.17*0.3)
        else: # A o nulo
            table_data.append(0.0)

        if self.object.tech_33_p1 == 'E': 
            table_data.append(0.17*1.0)
        elif self.object.tech_33_p1 == 'D':
            table_data.append(0.17*0.7)
        elif self.object.tech_33_p1 == 'C':
            table_data.append(0.17*0.5)
        elif self.object.tech_33_p1 == 'B':
            table_data.append(0.17*0.3)
        else: # A o nulo
            table_data.append(0.0)
  
        if self.object.tech_33_p2 == 'E': 
            table_data.append(0.17*1.0)
        elif self.object.tech_33_p2 == 'D':
            table_data.append(0.17*0.7)
        elif self.object.tech_33_p2 == 'C':
            table_data.append(0.17*0.5)
        elif self.object.tech_33_p2 == 'B':
            table_data.append(0.17*0.3)
        else: # A o nulo
            table_data.append(0.0)
       #tech 3.4
        if self.object.tech_34_act == 'E': 
            table_data.append(0.15*1.0)
        elif self.object.tech_34_act == 'D':
            table_data.append(0.15*0.7)
        elif self.object.tech_34_act == 'C':
            table_data.append(0.15*0.5)
        elif self.object.tech_34_act == 'B':
            table_data.append(0.15*0.3)
        else: # A o nulo
            table_data.append(0.0)

        if self.object.tech_34_p1 == 'E': 
            table_data.append(0.15*1.0)
        elif self.object.tech_34_p1 == 'D':
            table_data.append(0.15*0.7)
        elif self.object.tech_34_p1 == 'C':
            table_data.append(0.15*0.5)
        elif self.object.tech_34_p1 == 'B':
            table_data.append(0.15*0.3)
        else: # A o nulo
            table_data.append(0.0)
  
        if self.object.tech_34_p2 == 'E': 
            table_data.append(0.15*1.0)
        elif self.object.tech_34_p2 == 'D':
            table_data.append(0.15*0.7)
        elif self.object.tech_34_p2 == 'C':
            table_data.append(0.15*0.5)
        elif self.object.tech_34_p2 == 'B':
            table_data.append(0.15*0.3)
        else: # A o nulo
            table_data.append(0.0)
       #tech 3.5
        if self.object.tech_35_act == 'E': 
            table_data.append(0.17*1.0)
        elif self.object.tech_35_act == 'D':
            table_data.append(0.17*0.7)
        elif self.object.tech_35_act == 'C':
            table_data.append(0.17*0.5)
        elif self.object.tech_35_act == 'B':
            table_data.append(0.17*0.3)
        else: # A o nulo
            table_data.append(0.0)

        if self.object.tech_35_p1 == 'E': 
            table_data.append(0.17*1.0)
        elif self.object.tech_35_p1 == 'D':
            table_data.append(0.17*0.7)
        elif self.object.tech_35_p1 == 'C':
            table_data.append(0.17*0.5)
        elif self.object.tech_35_p1 == 'B':
            table_data.append(0.17*0.3)
        else: # A o nulo
            table_data.append(0.0)
  
        if self.object.tech_35_p2 == 'E': 
            table_data.append(0.17*1.0)
        elif self.object.tech_35_p2 == 'D':
            table_data.append(0.17*0.7)
        elif self.object.tech_35_p2 == 'C':
            table_data.append(0.17*0.5)
        elif self.object.tech_35_p2 == 'B':
            table_data.append(0.17*0.3)
        else: # A o nulo
            table_data.append(0.0)
       #tech 3.6
        if self.object.tech_36_act == 'E': 
            table_data.append(0.17*1.0)
        elif self.object.tech_36_act == 'D':
            table_data.append(0.17*0.7)
        elif self.object.tech_36_act == 'C':
            table_data.append(0.17*0.5)
        elif self.object.tech_36_act == 'B':
            table_data.append(0.17*0.3)
        else: # A o nulo
            table_data.append(0.0)

        if self.object.tech_36_p1 == 'E': 
            table_data.append(0.17*1.0)
        elif self.object.tech_36_p1 == 'D':
            table_data.append(0.17*0.7)
        elif self.object.tech_36_p1 == 'C':
            table_data.append(0.17*0.5)
        elif self.object.tech_36_p1 == 'B':
            table_data.append(0.17*0.3)
        else: # A o nulo
            table_data.append(0.0)
  
        if self.object.tech_36_p2 == 'E': 
            table_data.append(0.17*1.0)
        elif self.object.tech_36_p2 == 'D':
            table_data.append(0.17*0.7)
        elif self.object.tech_36_p2 == 'C':
            table_data.append(0.17*0.5)
        elif self.object.tech_36_p2 == 'B':
            table_data.append(0.17*0.3)
        else: # A o nulo
            table_data.append(0.0)
       #tech 4.1
        if self.object.tech_41_act == 'E': 
            table_data.append(0.17*1.0)
        elif self.object.tech_41_act == 'D':
            table_data.append(0.17*0.7)
        elif self.object.tech_41_act == 'C':
            table_data.append(0.17*0.5)
        elif self.object.tech_41_act == 'B':
            table_data.append(0.17*0.3)
        else: # A o nulo
            table_data.append(0.0)

        if self.object.tech_41_p1 == 'E': 
            table_data.append(0.17*1.0)
        elif self.object.tech_41_p1 == 'D':
            table_data.append(0.17*0.7)
        elif self.object.tech_41_p1 == 'C':
            table_data.append(0.17*0.5)
        elif self.object.tech_41_p1 == 'B':
            table_data.append(0.17*0.3)
        else: # A o nulo
            table_data.append(0.0)
  
        if self.object.tech_41_p2 == 'E': 
            table_data.append(0.17*1.0)
        elif self.object.tech_41_p2 == 'D':
            table_data.append(0.17*0.7)
        elif self.object.tech_41_p2 == 'C':
            table_data.append(0.17*0.5)
        elif self.object.tech_41_p2 == 'B':
            table_data.append(0.17*0.3)
        else: # A o nulo
            table_data.append(0.0)
       #tech 4.2
        if self.object.tech_42_act == 'E': 
            table_data.append(0.15*1.0)
        elif self.object.tech_42_act == 'D':
            table_data.append(0.15*0.7)
        elif self.object.tech_42_act == 'C':
            table_data.append(0.15*0.5)
        elif self.object.tech_42_act == 'B':
            table_data.append(0.15*0.3)
        else: # A o nulo
            table_data.append(0.0)

        if self.object.tech_42_p1 == 'E': 
            table_data.append(0.15*1.0)
        elif self.object.tech_42_p1 == 'D':
            table_data.append(0.15*0.7)
        elif self.object.tech_42_p1 == 'C':
            table_data.append(0.15*0.5)
        elif self.object.tech_42_p1 == 'B':
            table_data.append(0.15*0.3)
        else: # A o nulo
            table_data.append(0.0)
  
        if self.object.tech_42_p2 == 'E': 
            table_data.append(0.15*1.0)
        elif self.object.tech_42_p2 == 'D':
            table_data.append(0.15*0.7)
        elif self.object.tech_42_p2 == 'C':
            table_data.append(0.15*0.5)
        elif self.object.tech_42_p2 == 'B':
            table_data.append(0.15*0.3)
        else: # A o nulo
            table_data.append(0.0)
       #tech 4.3
        if self.object.tech_43_act == 'E': 
            table_data.append(0.19*1.0)
        elif self.object.tech_43_act == 'D':
            table_data.append(0.19*0.7)
        elif self.object.tech_43_act == 'C':
            table_data.append(0.19*0.5)
        elif self.object.tech_43_act == 'B':
            table_data.append(0.19*0.3)
        else: # A o nulo
            table_data.append(0.0)

        if self.object.tech_43_p1 == 'E': 
            table_data.append(0.19*1.0)
        elif self.object.tech_43_p1 == 'D':
            table_data.append(0.19*0.7)
        elif self.object.tech_43_p1 == 'C':
            table_data.append(0.19*0.5)
        elif self.object.tech_43_p1 == 'B':
            table_data.append(0.19*0.3)
        else: # A o nulo
            table_data.append(0.0)
  
        if self.object.tech_43_p2 == 'E': 
            table_data.append(0.19*1.0)
        elif self.object.tech_43_p2 == 'D':
            table_data.append(0.19*0.7)
        elif self.object.tech_43_p2 == 'C':
            table_data.append(0.19*0.5)
        elif self.object.tech_43_p2 == 'B':
            table_data.append(0.19*0.3)
        else: # A o nulo
            table_data.append(0.0)
        #tech 4.4
        if self.object.tech_44_act == 'F': 
            table_data.append(0.15*1.0)
        elif self.object.tech_44_act == 'E':
            table_data.append(0.15*0.7)
        elif self.object.tech_44_act == 'D':
            table_data.append(0.15*0.5)
        elif self.object.tech_44_act == 'C':
            table_data.append(0.15*0.3)
        elif self.object.tech_44_act == 'B':
            table_data.append(0.15*0.3)
        else: # A o nulo
            table_data.append(0.0)

        if self.object.tech_44_p1 == 'F': 
            table_data.append(0.15*1.0)
        elif self.object.tech_44_p1 == 'E':
            table_data.append(0.15*0.7)
        elif self.object.tech_44_p1 == 'D':
            table_data.append(0.15*0.5)
        elif self.object.tech_44_p1 == 'C':
            table_data.append(0.15*0.3)
        elif self.object.tech_44_p1 == 'B':
            table_data.append(0.15*0.3)
        else: # A o nulo
            table_data.append(0.0)
  
        if self.object.tech_44_p2 == 'F': 
            table_data.append(0.15*1.0)
        elif self.object.tech_44_p2 == 'E':
            table_data.append(0.15*0.7)
        elif self.object.tech_44_p2 == 'D':
            table_data.append(0.15*0.5)
        elif self.object.tech_44_p2 == 'C':
            table_data.append(0.15*0.3)
        elif self.object.tech_44_p2 == 'B':
            table_data.append(0.15*0.3)
        else: # A o nulo
            table_data.append(0.0)
        #tech 4.5
        if self.object.tech_45_act == 'D': 
            table_data.append(0.19*1.0)
        elif self.object.tech_45_act == 'C':
            table_data.append(0.19*0.7)
        elif self.object.tech_45_act == 'B':
            table_data.append(0.19*0.5)
        else: # A o nulo
            table_data.append(0.0)

        if self.object.tech_45_p1 == 'D': 
            table_data.append(0.19*1.0)
        elif self.object.tech_45_p1 == 'C':
            table_data.append(0.19*0.7)
        elif self.object.tech_45_p1 == 'B':
            table_data.append(0.19*0.5)
        else: # A o nulo
            table_data.append(0.0)
  
        if self.object.tech_45_p2 == 'D': 
            table_data.append(0.19*1.0)
        elif self.object.tech_45_p2 == 'C':
            table_data.append(0.19*0.7)
        elif self.object.tech_45_p2 == 'B':
            table_data.append(0.19*0.5)
        else: # A o nulo
            table_data.append(0.0)
        #tech 4.6
        if self.object.tech_46_act == 'D': 
            table_data.append(0.15*1.0)
        elif self.object.tech_46_act == 'C':
            table_data.append(0.15*0.7)
        elif self.object.tech_46_act == 'B':
            table_data.append(0.15*0.5)
        else: # A o nulo
            table_data.append(0.0)

        if self.object.tech_46_p1 == 'D': 
            table_data.append(0.15*1.0)
        elif self.object.tech_46_p1 == 'C':
            table_data.append(0.15*0.7)
        elif self.object.tech_46_p1 == 'B':
            table_data.append(0.15*0.5)
        else: # A o nulo
            table_data.append(0.0)
  
        if self.object.tech_46_p2 == 'D': 
            table_data.append(0.15*1.0)
        elif self.object.tech_46_p2 == 'C':
            table_data.append(0.15*0.7)
        elif self.object.tech_46_p2 == 'B':
            table_data.append(0.15*0.5)
        else: # A o nulo
            table_data.append(0.0)
        #tech 5.1
        if self.object.tech_51_act == 'D': 
            table_data.append(0.4*1.0)
        elif self.object.tech_51_act == 'C':
            table_data.append(0.4*0.5)
        elif self.object.tech_51_act == 'B':
            table_data.append(0.4*0.3)
        else: # A o nulo
            table_data.append(0.0)

        if self.object.tech_51_p1 == 'D': 
            table_data.append(0.4*1.0)
        elif self.object.tech_51_p1 == 'C':
            table_data.append(0.4*0.5)
        elif self.object.tech_51_p1 == 'B':
            table_data.append(0.4*0.3)
        else: # A o nulo
            table_data.append(0.0)
  
        if self.object.tech_51_p2 == 'D': 
            table_data.append(0.4*1.0)
        elif self.object.tech_51_p2 == 'C':
            table_data.append(0.4*0.5)
        elif self.object.tech_51_p2 == 'B':
            table_data.append(0.4*0.3)
        else: # A o nulo
            table_data.append(0.0)
       #tech 5.2
        if self.object.tech_52_act == 'E': 
            table_data.append(0.6*1.0)
        elif self.object.tech_52_act == 'D':
            table_data.append(0.6*0.7)
        elif self.object.tech_52_act == 'C':
            table_data.append(0.6*0.5)
        elif self.object.tech_52_act == 'B':
            table_data.append(0.6*0.3)
        else: # A o nulo
            table_data.append(0.0)

        if self.object.tech_52_p1 == 'E': 
            table_data.append(0.6*1.0)
        elif self.object.tech_52_p1 == 'D':
            table_data.append(0.6*0.7)
        elif self.object.tech_52_p1 == 'C':
            table_data.append(0.6*0.5)
        elif self.object.tech_52_p1 == 'B':
            table_data.append(0.6*0.3)
        else: # A o nulo
            table_data.append(0.0)
  
        if self.object.tech_52_p2 == 'E': 
            table_data.append(0.6*1.0)
        elif self.object.tech_52_p2 == 'D':
            table_data.append(0.6*0.7)
        elif self.object.tech_52_p2 == 'C':
            table_data.append(0.6*0.5)
        elif self.object.tech_52_p2 == 'B':
            table_data.append(0.6*0.3)
        else: # A o nulo
            table_data.append(0.0)

        return table_data

    def get_table_data_cust(self):
        table_data = [] #lista vacia para almacenar resultados 
        #############CUST#################
                #cust 1.1
        if self.object.cust_11_act == 'D': 
            table_data.append(0.25*1.0)
        elif self.object.cust_11_act == 'C':
            table_data.append(0.25*0.7)
        elif self.object.cust_11_act == 'B':
            table_data.append(0.25*0.5)
        else: # A o nulo
            table_data.append(0.0)

        if self.object.cust_11_p1 == 'D': 
            table_data.append(0.25*1.0)
        elif self.object.cust_11_p1 == 'C':
            table_data.append(0.25*0.7)
        elif self.object.cust_11_p1 == 'B':
            table_data.append(0.25*0.5)
        else: # A o nulo
            table_data.append(0.0)
  
        if self.object.cust_11_p2 == 'D': 
            table_data.append(0.25*1.0)
        elif self.object.cust_11_p2 == 'C':
            table_data.append(0.25*0.7)
        elif self.object.cust_11_p2 == 'B':
            table_data.append(0.25*0.5)
        else: # A o nulo
            table_data.append(0.0)
        #cust 1.2
        if self.object.cust_12_act == 'D': 
            table_data.append(0.25*1.0)
        elif self.object.cust_12_act == 'C':
            table_data.append(0.25*0.7)
        elif self.object.cust_12_act == 'B':
            table_data.append(0.25*0.5)
        else: # A o nulo
            table_data.append(0.0)

        if self.object.cust_12_p1 == 'D': 
            table_data.append(0.25*1.0)
        elif self.object.cust_12_p1 == 'C':
            table_data.append(0.25*0.7)
        elif self.object.cust_12_p1 == 'B':
            table_data.append(0.25*0.5)
        else: # A o nulo
            table_data.append(0.0)
  
        if self.object.cust_12_p2 == 'D': 
            table_data.append(0.25*1.0)
        elif self.object.cust_12_p2 == 'C':
            table_data.append(0.25*0.7)
        elif self.object.cust_12_p2 == 'B':
            table_data.append(0.25*0.5)
        else: # A o nulo
            table_data.append(0.0)
        #cust 1.3
        if self.object.cust_13_act == 'D': 
            table_data.append(0.25*1.0)
        elif self.object.cust_13_act == 'C':
            table_data.append(0.25*0.7)
        elif self.object.cust_13_act == 'B':
            table_data.append(0.25*0.5)
        else: # A o nulo
            table_data.append(0.0)

        if self.object.cust_13_p1 == 'D': 
            table_data.append(0.25*1.0)
        elif self.object.cust_13_p1 == 'C':
            table_data.append(0.25*0.7)
        elif self.object.cust_13_p1 == 'B':
            table_data.append(0.25*0.5)
        else: # A o nulo
            table_data.append(0.0)
  
        if self.object.cust_13_p2 == 'D': 
            table_data.append(0.25*1.0)
        elif self.object.cust_13_p2 == 'C':
            table_data.append(0.25*0.7)
        elif self.object.cust_13_p2 == 'B':
            table_data.append(0.25*0.5)
        else: # A o nulo
            table_data.append(0.0)
        #cust 1.4
        if self.object.cust_14_act == 'C': 
            table_data.append(0.25*1.0)
        elif self.object.cust_14_act == 'B':
            table_data.append(0.25*0.5)
        else: # A o nulo
            table_data.append(0.0)

        if self.object.cust_14_p1 == 'C': 
            table_data.append(0.25*1.0)
        elif self.object.cust_14_p1 == 'B':
            table_data.append(0.25*0.5)
        else: # A o nulo
            table_data.append(0.0)
  
        if self.object.cust_14_p2 == 'C': 
            table_data.append(0.25*1.0)
        elif self.object.cust_14_p2 == 'B':
            table_data.append(0.25*0.5)
        else: # A o nulo
            table_data.append(0.0)
        #cust 2.1
        if self.object.cust_21_act == 'D': 
            table_data.append(0.17*1.0)
        elif self.object.cust_21_act == 'C':
            table_data.append(0.17*0.7)
        elif self.object.cust_21_act == 'B':
            table_data.append(0.17*0.3)
        else: # A o nulo
            table_data.append(0.0)

        if self.object.cust_21_p1 == 'D': 
            table_data.append(0.17*1.0)
        elif self.object.cust_21_p1 == 'C':
            table_data.append(0.17*0.7)
        elif self.object.cust_21_p1 == 'B':
            table_data.append(0.17*0.3)
        else: # A o nulo
            table_data.append(0.0)
  
        if self.object.cust_21_p2 == 'D': 
            table_data.append(0.17*1.0)
        elif self.object.cust_21_p2 == 'C':
            table_data.append(0.17*0.7)
        elif self.object.cust_21_p2 == 'B':
            table_data.append(0.17*0.3)
        else: # A o nulo
            table_data.append(0.0)
       #cust 2.2
        if self.object.cust_22_act == 'E': 
            table_data.append(0.17*1.0)
        elif self.object.cust_22_act == 'D':
            table_data.append(0.17*0.7)
        elif self.object.cust_22_act == 'C':
            table_data.append(0.17*0.5)
        elif self.object.cust_22_act == 'B':
            table_data.append(0.17*0.3)
        else: # A o nulo
            table_data.append(0.0)

        if self.object.cust_22_p1 == 'E': 
            table_data.append(0.17*1.0)
        elif self.object.cust_22_p1 == 'D':
            table_data.append(0.17*0.7)
        elif self.object.cust_22_p1 == 'C':
            table_data.append(0.17*0.5)
        elif self.object.cust_22_p1 == 'B':
            table_data.append(0.17*0.3)
        else: # A o nulo
            table_data.append(0.0)
  
        if self.object.cust_22_p2 == 'E': 
            table_data.append(0.17*1.0)
        elif self.object.cust_22_p2 == 'D':
            table_data.append(0.17*0.7)
        elif self.object.cust_22_p2 == 'C':
            table_data.append(0.17*0.5)
        elif self.object.cust_22_p2 == 'B':
            table_data.append(0.17*0.3)
        else: # A o nulo
            table_data.append(0.0)
       #cust 2.3
        if self.object.cust_23_act == 'E': 
            table_data.append(0.15*1.0)
        elif self.object.cust_23_act == 'D':
            table_data.append(0.15*0.7)
        elif self.object.cust_23_act == 'C':
            table_data.append(0.15*0.5)
        elif self.object.cust_23_act == 'B':
            table_data.append(0.15*0.3)
        else: # A o nulo
            table_data.append(0.0)

        if self.object.cust_23_p1 == 'E': 
            table_data.append(0.15*1.0)
        elif self.object.cust_23_p1 == 'D':
            table_data.append(0.15*0.7)
        elif self.object.cust_23_p1 == 'C':
            table_data.append(0.15*0.5)
        elif self.object.cust_23_p1 == 'B':
            table_data.append(0.15*0.3)
        else: # A o nulo
            table_data.append(0.0)
  
        if self.object.cust_23_p2 == 'E': 
            table_data.append(0.15*1.0)
        elif self.object.cust_23_p2 == 'D':
            table_data.append(0.15*0.7)
        elif self.object.cust_23_p2 == 'C':
            table_data.append(0.15*0.5)
        elif self.object.cust_23_p2 == 'B':
            table_data.append(0.15*0.3)
        else: # A o nulo
            table_data.append(0.0)
        #cust 2.4
        if self.object.cust_24_act == 'D': 
            table_data.append(0.17*1.0)
        elif self.object.cust_24_act == 'C':
            table_data.append(0.17*0.7)
        elif self.object.cust_24_act == 'B':
            table_data.append(0.17*0.3)
        else: # A o nulo
            table_data.append(0.0)

        if self.object.cust_24_p1 == 'D': 
            table_data.append(0.17*1.0)
        elif self.object.cust_24_p1 == 'C':
            table_data.append(0.17*0.7)
        elif self.object.cust_24_p1 == 'B':
            table_data.append(0.17*0.3)
        else: # A o nulo
            table_data.append(0.0)
  
        if self.object.cust_24_p2 == 'D': 
            table_data.append(0.17*1.0)
        elif self.object.cust_24_p2 == 'C':
            table_data.append(0.17*0.7)
        elif self.object.cust_24_p2 == 'B':
            table_data.append(0.17*0.3)
        else: # A o nulo
            table_data.append(0.0)
        #cust 2.5
        if self.object.cust_25_act == 'D': 
            table_data.append(0.17*1.0)
        elif self.object.cust_25_act == 'C':
            table_data.append(0.17*0.7)
        elif self.object.cust_25_act == 'B':
            table_data.append(0.17*0.3)
        else: # A o nulo
            table_data.append(0.0)

        if self.object.cust_25_p1 == 'D': 
            table_data.append(0.17*1.0)
        elif self.object.cust_25_p1 == 'C':
            table_data.append(0.17*0.7)
        elif self.object.cust_25_p1 == 'B':
            table_data.append(0.17*0.3)
        else: # A o nulo
            table_data.append(0.0)
  
        if self.object.cust_25_p2 == 'D': 
            table_data.append(0.17*1.0)
        elif self.object.cust_25_p2 == 'C':
            table_data.append(0.17*0.7)
        elif self.object.cust_25_p2 == 'B':
            table_data.append(0.17*0.3)
        else: # A o nulo
            table_data.append(0.0)
       #cust 2.6
        if self.object.cust_26_act == 'E': 
            table_data.append(0.17*1.0)
        elif self.object.cust_26_act == 'D':
            table_data.append(0.17*0.7)
        elif self.object.cust_26_act == 'C':
            table_data.append(0.17*0.5)
        elif self.object.cust_26_act == 'B':
            table_data.append(0.17*0.3)
        else: # A o nulo
            table_data.append(0.0)

        if self.object.cust_26_p1 == 'E': 
            table_data.append(0.17*1.0)
        elif self.object.cust_26_p1 == 'D':
            table_data.append(0.17*0.7)
        elif self.object.cust_26_p1 == 'C':
            table_data.append(0.17*0.5)
        elif self.object.cust_26_p1 == 'B':
            table_data.append(0.17*0.3)
        else: # A o nulo
            table_data.append(0.0)
  
        if self.object.cust_26_p2 == 'E': 
            table_data.append(0.17*1.0)
        elif self.object.cust_26_p2 == 'D':
            table_data.append(0.17*0.7)
        elif self.object.cust_26_p2 == 'C':
            table_data.append(0.17*0.5)
        elif self.object.cust_26_p2 == 'B':
            table_data.append(0.17*0.3)
        else: # A o nulo
            table_data.append(0.0)
        #cust 3.1
        if self.object.cust_31_act == 'D': 
            table_data.append(0.1*1.0)
        elif self.object.cust_31_act == 'C':
            table_data.append(0.1*0.7)
        elif self.object.cust_31_act == 'B':
            table_data.append(0.1*0.3)
        else: # A o nulo
            table_data.append(0.0)

        if self.object.cust_31_p1 == 'D': 
            table_data.append(0.1*1.0)
        elif self.object.cust_31_p1 == 'C':
            table_data.append(0.1*0.7)
        elif self.object.cust_31_p1 == 'B':
            table_data.append(0.1*0.3)
        else: # A o nulo
            table_data.append(0.0)
  
        if self.object.cust_31_p2 == 'D': 
            table_data.append(0.1*1.0)
        elif self.object.cust_31_p2 == 'C':
            table_data.append(0.1*0.7)
        elif self.object.cust_31_p2 == 'B':
            table_data.append(0.1*0.3)
        else: # A o nulo
            table_data.append(0.0)
       #cust 3.2
        if self.object.cust_32_act == 'E': 
            table_data.append(0.12*1.0)
        elif self.object.cust_32_act == 'D':
            table_data.append(0.12*0.7)
        elif self.object.cust_32_act == 'C':
            table_data.append(0.12*0.5)
        elif self.object.cust_32_act == 'B':
            table_data.append(0.12*0.3)
        else: # A o nulo
            table_data.append(0.0)

        if self.object.cust_32_p1 == 'E': 
            table_data.append(0.12*1.0)
        elif self.object.cust_32_p1 == 'D':
            table_data.append(0.12*0.7)
        elif self.object.cust_32_p1 == 'C':
            table_data.append(0.12*0.5)
        elif self.object.cust_32_p1 == 'B':
            table_data.append(0.12*0.3)
        else: # A o nulo
            table_data.append(0.0)
  
        if self.object.cust_32_p2 == 'E': 
            table_data.append(0.12*1.0)
        elif self.object.cust_32_p2 == 'D':
            table_data.append(0.12*0.7)
        elif self.object.cust_32_p2 == 'C':
            table_data.append(0.12*0.5)
        elif self.object.cust_32_p2 == 'B':
            table_data.append(0.12*0.3)
        else: # A o nulo
            table_data.append(0.0)
       #cust 3.3
        if self.object.cust_33_act == 'E': 
            table_data.append(0.1*1.0)
        elif self.object.cust_33_act == 'D':
            table_data.append(0.1*0.7)
        elif self.object.cust_33_act == 'C':
            table_data.append(0.1*0.5)
        elif self.object.cust_33_act == 'B':
            table_data.append(0.1*0.3)
        else: # A o nulo
            table_data.append(0.0)

        if self.object.cust_33_p1 == 'E': 
            table_data.append(0.1*1.0)
        elif self.object.cust_33_p1 == 'D':
            table_data.append(0.1*0.7)
        elif self.object.cust_33_p1 == 'C':
            table_data.append(0.1*0.5)
        elif self.object.cust_33_p1 == 'B':
            table_data.append(0.1*0.3)
        else: # A o nulo
            table_data.append(0.0)
  
        if self.object.cust_33_p2 == 'E': 
            table_data.append(0.1*1.0)
        elif self.object.cust_33_p2 == 'D':
            table_data.append(0.1*0.7)
        elif self.object.cust_33_p2 == 'C':
            table_data.append(0.1*0.5)
        elif self.object.cust_33_p2 == 'B':
            table_data.append(0.1*0.3)
        else: # A o nulo
            table_data.append(0.0)
       #cust 3.4
        if self.object.cust_34_act == 'E': 
            table_data.append(0.12*1.0)
        elif self.object.cust_34_act == 'D':
            table_data.append(0.12*0.7)
        elif self.object.cust_34_act == 'C':
            table_data.append(0.12*0.5)
        elif self.object.cust_34_act == 'B':
            table_data.append(0.12*0.3)
        else: # A o nulo
            table_data.append(0.0)

        if self.object.cust_34_p1 == 'E': 
            table_data.append(0.12*1.0)
        elif self.object.cust_34_p1 == 'D':
            table_data.append(0.12*0.7)
        elif self.object.cust_34_p1 == 'C':
            table_data.append(0.12*0.5)
        elif self.object.cust_34_p1 == 'B':
            table_data.append(0.12*0.3)
        else: # A o nulo
            table_data.append(0.0)
  
        if self.object.cust_34_p2 == 'E': 
            table_data.append(0.12*1.0)
        elif self.object.cust_34_p2 == 'D':
            table_data.append(0.12*0.7)
        elif self.object.cust_34_p2 == 'C':
            table_data.append(0.12*0.5)
        elif self.object.cust_34_p2 == 'B':
            table_data.append(0.12*0.3)
        else: # A o nulo
            table_data.append(0.0)
       #cust 3.5
        if self.object.cust_35_act == 'E': 
            table_data.append(0.12*1.0)
        elif self.object.cust_35_act == 'D':
            table_data.append(0.12*0.7)
        elif self.object.cust_35_act == 'C':
            table_data.append(0.12*0.5)
        elif self.object.cust_35_act == 'B':
            table_data.append(0.12*0.3)
        else: # A o nulo
            table_data.append(0.0)

        if self.object.cust_35_p1 == 'E': 
            table_data.append(0.12*1.0)
        elif self.object.cust_35_p1 == 'D':
            table_data.append(0.12*0.7)
        elif self.object.cust_35_p1 == 'C':
            table_data.append(0.12*0.5)
        elif self.object.cust_35_p1 == 'B':
            table_data.append(0.12*0.3)
        else: # A o nulo
            table_data.append(0.0)
  
        if self.object.cust_35_p2 == 'E': 
            table_data.append(0.12*1.0)
        elif self.object.cust_35_p2 == 'D':
            table_data.append(0.12*0.7)
        elif self.object.cust_35_p2 == 'C':
            table_data.append(0.12*0.5)
        elif self.object.cust_35_p2 == 'B':
            table_data.append(0.12*0.3)
        else: # A o nulo
            table_data.append(0.0)
      #cust 3.6
        if self.object.cust_36_act == 'E': 
            table_data.append(0.12*1.0)
        elif self.object.cust_36_act == 'D':
            table_data.append(0.12*0.7)
        elif self.object.cust_36_act == 'C':
            table_data.append(0.12*0.5)
        elif self.object.cust_36_act == 'B':
            table_data.append(0.12*0.3)
        else: # A o nulo
            table_data.append(0.0)

        if self.object.cust_36_p1 == 'E': 
            table_data.append(0.12*1.0)
        elif self.object.cust_36_p1 == 'D':
            table_data.append(0.12*0.7)
        elif self.object.cust_36_p1 == 'C':
            table_data.append(0.12*0.5)
        elif self.object.cust_36_p1 == 'B':
            table_data.append(0.12*0.3)
        else: # A o nulo
            table_data.append(0.0)
  
        if self.object.cust_36_p2 == 'E': 
            table_data.append(0.12*1.0)
        elif self.object.cust_36_p2 == 'D':
            table_data.append(0.12*0.7)
        elif self.object.cust_36_p2 == 'C':
            table_data.append(0.12*0.5)
        elif self.object.cust_36_p2 == 'B':
            table_data.append(0.12*0.3)
        else: # A o nulo
            table_data.append(0.0)
       #cust 3.7
        if self.object.cust_37_act == 'E': 
            table_data.append(0.1*1.0)
        elif self.object.cust_37_act == 'D':
            table_data.append(0.1*0.7)
        elif self.object.cust_37_act == 'C':
            table_data.append(0.1*0.5)
        elif self.object.cust_37_act == 'B':
            table_data.append(0.1*0.3)
        else: # A o nulo
            table_data.append(0.0)

        if self.object.cust_37_p1 == 'E': 
            table_data.append(0.1*1.0)
        elif self.object.cust_37_p1 == 'D':
            table_data.append(0.1*0.7)
        elif self.object.cust_37_p1 == 'C':
            table_data.append(0.1*0.5)
        elif self.object.cust_37_p1 == 'B':
            table_data.append(0.1*0.3)
        else: # A o nulo
            table_data.append(0.0)
  
        if self.object.cust_37_p2 == 'E': 
            table_data.append(0.1*1.0)
        elif self.object.cust_37_p2 == 'D':
            table_data.append(0.1*0.7)
        elif self.object.cust_37_p2 == 'C':
            table_data.append(0.1*0.5)
        elif self.object.cust_37_p2 == 'B':
            table_data.append(0.1*0.3)
        else: # A o nulo
            table_data.append(0.0)
        #cust 3.8
        if self.object.cust_38_act == 'D': 
            table_data.append(0.12*1.0)
        elif self.object.cust_38_act == 'C':
            table_data.append(0.12*0.7)
        elif self.object.cust_38_act == 'B':
            table_data.append(0.12*0.5)
        else: # A o nulo
            table_data.append(0.0)

        if self.object.cust_38_p1 == 'D': 
            table_data.append(0.12*1.0)
        elif self.object.cust_38_p1 == 'C':
            table_data.append(0.12*0.7)
        elif self.object.cust_38_p1 == 'B':
            table_data.append(0.12*0.5)
        else: # A o nulo
            table_data.append(0.0)
  
        if self.object.cust_38_p2 == 'D': 
            table_data.append(0.12*1.0)
        elif self.object.cust_38_p2 == 'C':
            table_data.append(0.12*0.7)
        elif self.object.cust_38_p2 == 'B':
            table_data.append(0.12*0.5)
        else: # A o nulo
            table_data.append(0.0)
       #cust 3.9
        if self.object.cust_39_act == 'E': 
            table_data.append(0.1*1.0)
        elif self.object.cust_39_act == 'D':
            table_data.append(0.1*0.7)
        elif self.object.cust_39_act == 'C':
            table_data.append(0.1*0.5)
        elif self.object.cust_39_act == 'B':
            table_data.append(0.1*0.3)
        else: # A o nulo
            table_data.append(0.0)

        if self.object.cust_39_p1 == 'E': 
            table_data.append(0.1*1.0)
        elif self.object.cust_39_p1 == 'D':
            table_data.append(0.1*0.7)
        elif self.object.cust_39_p1 == 'C':
            table_data.append(0.1*0.5)
        elif self.object.cust_39_p1 == 'B':
            table_data.append(0.1*0.3)
        else: # A o nulo
            table_data.append(0.0)
  
        if self.object.cust_39_p2 == 'E': 
            table_data.append(0.1*1.0)
        elif self.object.cust_39_p2 == 'D':
            table_data.append(0.1*0.7)
        elif self.object.cust_39_p2 == 'C':
            table_data.append(0.1*0.5)
        elif self.object.cust_39_p2 == 'B':
            table_data.append(0.1*0.3)
        else: # A o nulo
            table_data.append(0.0)
        #cust 4.1
        if self.object.cust_41_act == 'D': 
            table_data.append(0.15*1.0)
        elif self.object.cust_41_act == 'C':
            table_data.append(0.15*0.7)
        elif self.object.cust_41_act == 'B':
            table_data.append(0.15*0.5)
        else: # A o nulo
            table_data.append(0.0)

        if self.object.cust_41_p1 == 'D': 
            table_data.append(0.15*1.0)
        elif self.object.cust_41_p1 == 'C':
            table_data.append(0.15*0.7)
        elif self.object.cust_41_p1 == 'B':
            table_data.append(0.15*0.5)
        else: # A o nulo
            table_data.append(0.0)
  
        if self.object.cust_41_p2 == 'D': 
            table_data.append(0.15*1.0)
        elif self.object.cust_41_p2 == 'C':
            table_data.append(0.15*0.7)
        elif self.object.cust_41_p2 == 'B':
            table_data.append(0.15*0.5)
        else: # A o nulo
            table_data.append(0.0)
       #cust 4.2
        if self.object.cust_42_act == 'E': 
            table_data.append(0.13*1.0)
        elif self.object.cust_42_act == 'D':
            table_data.append(0.13*0.7)
        elif self.object.cust_42_act == 'C':
            table_data.append(0.13*0.5)
        elif self.object.cust_42_act == 'B':
            table_data.append(0.13*0.3)
        else: # A o nulo
            table_data.append(0.0)

        if self.object.cust_42_p1 == 'E': 
            table_data.append(0.13*1.0)
        elif self.object.cust_42_p1 == 'D':
            table_data.append(0.13*0.7)
        elif self.object.cust_42_p1 == 'C':
            table_data.append(0.13*0.5)
        elif self.object.cust_42_p1 == 'B':
            table_data.append(0.13*0.3)
        else: # A o nulo
            table_data.append(0.0)
  
        if self.object.cust_42_p2 == 'E': 
            table_data.append(0.13*1.0)
        elif self.object.cust_42_p2 == 'D':
            table_data.append(0.13*0.7)
        elif self.object.cust_42_p2 == 'C':
            table_data.append(0.13*0.5)
        elif self.object.cust_42_p2 == 'B':
            table_data.append(0.13*0.3)
        else: # A o nulo
            table_data.append(0.0)
       #cust 4.3
        if self.object.cust_43_act == 'E': 
            table_data.append(0.15*1.0)
        elif self.object.cust_43_act == 'D':
            table_data.append(0.15*0.7)
        elif self.object.cust_43_act == 'C':
            table_data.append(0.15*0.5)
        elif self.object.cust_43_act == 'B':
            table_data.append(0.15*0.3)
        else: # A o nulo
            table_data.append(0.0)

        if self.object.cust_43_p1 == 'E': 
            table_data.append(0.15*1.0)
        elif self.object.cust_43_p1 == 'D':
            table_data.append(0.15*0.7)
        elif self.object.cust_43_p1 == 'C':
            table_data.append(0.15*0.5)
        elif self.object.cust_43_p1 == 'B':
            table_data.append(0.15*0.3)
        else: # A o nulo
            table_data.append(0.0)
  
        if self.object.cust_43_p2 == 'E': 
            table_data.append(0.15*1.0)
        elif self.object.cust_43_p2 == 'D':
            table_data.append(0.15*0.7)
        elif self.object.cust_43_p2 == 'C':
            table_data.append(0.15*0.5)
        elif self.object.cust_43_p2 == 'B':
            table_data.append(0.15*0.3)
        else: # A o nulo
            table_data.append(0.0)
       #cust 4.4
        if self.object.cust_44_act == 'E': 
            table_data.append(0.15*1.0)
        elif self.object.cust_44_act == 'D':
            table_data.append(0.15*0.7)
        elif self.object.cust_44_act == 'C':
            table_data.append(0.15*0.5)
        elif self.object.cust_44_act == 'B':
            table_data.append(0.15*0.3)
        else: # A o nulo
            table_data.append(0.0)

        if self.object.cust_44_p1 == 'E': 
            table_data.append(0.15*1.0)
        elif self.object.cust_44_p1 == 'D':
            table_data.append(0.15*0.7)
        elif self.object.cust_44_p1 == 'C':
            table_data.append(0.15*0.5)
        elif self.object.cust_44_p1 == 'B':
            table_data.append(0.15*0.3)
        else: # A o nulo
            table_data.append(0.0)
  
        if self.object.cust_44_p2 == 'E': 
            table_data.append(0.15*1.0)
        elif self.object.cust_44_p2 == 'D':
            table_data.append(0.15*0.7)
        elif self.object.cust_44_p2 == 'C':
            table_data.append(0.15*0.5)
        elif self.object.cust_44_p2 == 'B':
            table_data.append(0.15*0.3)
        else: # A o nulo
            table_data.append(0.0)
       #cust 4.5
        if self.object.cust_45_act == 'E': 
            table_data.append(0.15*1.0)
        elif self.object.cust_45_act == 'D':
            table_data.append(0.15*0.7)
        elif self.object.cust_45_act == 'C':
            table_data.append(0.15*0.5)
        elif self.object.cust_45_act == 'B':
            table_data.append(0.15*0.3)
        else: # A o nulo
            table_data.append(0.0)

        if self.object.cust_45_p1 == 'E': 
            table_data.append(0.15*1.0)
        elif self.object.cust_45_p1 == 'D':
            table_data.append(0.15*0.7)
        elif self.object.cust_45_p1 == 'C':
            table_data.append(0.15*0.5)
        elif self.object.cust_45_p1 == 'B':
            table_data.append(0.15*0.3)
        else: # A o nulo
            table_data.append(0.0)
  
        if self.object.cust_45_p2 == 'E': 
            table_data.append(0.15*1.0)
        elif self.object.cust_45_p2 == 'D':
            table_data.append(0.15*0.7)
        elif self.object.cust_45_p2 == 'C':
            table_data.append(0.15*0.5)
        elif self.object.cust_45_p2 == 'B':
            table_data.append(0.15*0.3)
        else: # A o nulo
            table_data.append(0.0)
       #cust 4.6
        if self.object.cust_46_act == 'E': 
            table_data.append(0.15*1.0)
        elif self.object.cust_46_act == 'D':
            table_data.append(0.15*0.7)
        elif self.object.cust_46_act == 'C':
            table_data.append(0.15*0.5)
        elif self.object.cust_46_act == 'B':
            table_data.append(0.15*0.3)
        else: # A o nulo
            table_data.append(0.0)

        if self.object.cust_46_p1 == 'E': 
            table_data.append(0.15*1.0)
        elif self.object.cust_46_p1 == 'D':
            table_data.append(0.15*0.7)
        elif self.object.cust_46_p1 == 'C':
            table_data.append(0.15*0.5)
        elif self.object.cust_46_p1 == 'B':
            table_data.append(0.15*0.3)
        else: # A o nulo
            table_data.append(0.0)
  
        if self.object.cust_46_p2 == 'E': 
            table_data.append(0.15*1.0)
        elif self.object.cust_46_p2 == 'D':
            table_data.append(0.15*0.7)
        elif self.object.cust_46_p2 == 'C':
            table_data.append(0.15*0.5)
        elif self.object.cust_46_p2 == 'B':
            table_data.append(0.15*0.3)
        else: # A o nulo
            table_data.append(0.0)
       #cust 4.7
        if self.object.cust_47_act == 'E': 
            table_data.append(0.12*1.0)
        elif self.object.cust_47_act == 'D':
            table_data.append(0.12*0.7)
        elif self.object.cust_47_act == 'C':
            table_data.append(0.12*0.5)
        elif self.object.cust_47_act == 'B':
            table_data.append(0.12*0.3)
        else: # A o nulo
            table_data.append(0.0)

        if self.object.cust_47_p1 == 'E': 
            table_data.append(0.12*1.0)
        elif self.object.cust_47_p1 == 'D':
            table_data.append(0.12*0.7)
        elif self.object.cust_47_p1 == 'C':
            table_data.append(0.12*0.5)
        elif self.object.cust_47_p1 == 'B':
            table_data.append(0.12*0.3)
        else: # A o nulo
            table_data.append(0.0)
  
        if self.object.cust_47_p2 == 'E': 
            table_data.append(0.12*1.0)
        elif self.object.cust_47_p2 == 'D':
            table_data.append(0.12*0.7)
        elif self.object.cust_47_p2 == 'C':
            table_data.append(0.12*0.5)
        elif self.object.cust_47_p2 == 'B':
            table_data.append(0.12*0.3)
        else: # A o nulo
            table_data.append(0.0)
       #cust 5.1
        if self.object.cust_51_act == 'E': 
            table_data.append(0.22*1.0)
        elif self.object.cust_51_act == 'D':
            table_data.append(0.22*0.7)
        elif self.object.cust_51_act == 'C':
            table_data.append(0.22*0.5)
        elif self.object.cust_51_act == 'B':
            table_data.append(0.22*0.3)
        else: # A o nulo
            table_data.append(0.0)

        if self.object.cust_51_p1 == 'E': 
            table_data.append(0.22*1.0)
        elif self.object.cust_51_p1 == 'D':
            table_data.append(0.22*0.7)
        elif self.object.cust_51_p1 == 'C':
            table_data.append(0.22*0.5)
        elif self.object.cust_51_p1 == 'B':
            table_data.append(0.22*0.3)
        else: # A o nulo
            table_data.append(0.0)
  
        if self.object.cust_51_p2 == 'E': 
            table_data.append(0.22*1.0)
        elif self.object.cust_51_p2 == 'D':
            table_data.append(0.22*0.7)
        elif self.object.cust_51_p2 == 'C':
            table_data.append(0.22*0.5)
        elif self.object.cust_51_p2 == 'B':
            table_data.append(0.22*0.3)
        else: # A o nulo
            table_data.append(0.0)
       #cust 5.2
        if self.object.cust_52_act == 'E': 
            table_data.append(0.22*1.0)
        elif self.object.cust_52_act == 'D':
            table_data.append(0.22*0.7)
        elif self.object.cust_52_act == 'C':
            table_data.append(0.22*0.5)
        elif self.object.cust_52_act == 'B':
            table_data.append(0.22*0.3)
        else: # A o nulo
            table_data.append(0.0)

        if self.object.cust_52_p1 == 'E': 
            table_data.append(0.22*1.0)
        elif self.object.cust_52_p1 == 'D':
            table_data.append(0.22*0.7)
        elif self.object.cust_52_p1 == 'C':
            table_data.append(0.22*0.5)
        elif self.object.cust_52_p1 == 'B':
            table_data.append(0.22*0.3)
        else: # A o nulo
            table_data.append(0.0)
  
        if self.object.cust_52_p2 == 'E': 
            table_data.append(0.22*1.0)
        elif self.object.cust_52_p2 == 'D':
            table_data.append(0.22*0.7)
        elif self.object.cust_52_p2 == 'C':
            table_data.append(0.22*0.5)
        elif self.object.cust_52_p2 == 'B':
            table_data.append(0.22*0.3)
        else: # A o nulo
            table_data.append(0.0)
       #cust 5.3
        if self.object.cust_53_act == 'E': 
            table_data.append(0.22*1.0)
        elif self.object.cust_53_act == 'D':
            table_data.append(0.22*0.7)
        elif self.object.cust_53_act == 'C':
            table_data.append(0.22*0.5)
        elif self.object.cust_53_act == 'B':
            table_data.append(0.22*0.3)
        else: # A o nulo
            table_data.append(0.0)

        if self.object.cust_53_p1 == 'E': 
            table_data.append(0.22*1.0)
        elif self.object.cust_53_p1 == 'D':
            table_data.append(0.22*0.7)
        elif self.object.cust_53_p1 == 'C':
            table_data.append(0.22*0.5)
        elif self.object.cust_53_p1 == 'B':
            table_data.append(0.22*0.3)
        else: # A o nulo
            table_data.append(0.0)
  
        if self.object.cust_53_p2 == 'E': 
            table_data.append(0.22*1.0)
        elif self.object.cust_53_p2 == 'D':
            table_data.append(0.22*0.7)
        elif self.object.cust_53_p2 == 'C':
            table_data.append(0.22*0.5)
        elif self.object.cust_53_p2 == 'B':
            table_data.append(0.22*0.3)
        else: # A o nulo
            table_data.append(0.0)
        #cust 5.4
        if self.object.cust_54_act == 'D': 
            table_data.append(0.15*1.0)
        elif self.object.cust_54_act == 'C':
            table_data.append(0.15*0.7)
        elif self.object.cust_54_act == 'B':
            table_data.append(0.15*0.3)
        else: # A o nulo
            table_data.append(0.0)

        if self.object.cust_54_p1 == 'D': 
            table_data.append(0.15*1.0)
        elif self.object.cust_54_p1 == 'C':
            table_data.append(0.15*0.7)
        elif self.object.cust_54_p1 == 'B':
            table_data.append(0.15*0.3)
        else: # A o nulo
            table_data.append(0.0)
  
        if self.object.cust_54_p2 == 'D': 
            table_data.append(0.15*1.0)
        elif self.object.cust_54_p2 == 'C':
            table_data.append(0.15*0.7)
        elif self.object.cust_54_p2 == 'B':
            table_data.append(0.15*0.3)
        else: # A o nulo
            table_data.append(0.0)
        #cust 5.5
        if self.object.cust_55_act == 'D': 
            table_data.append(0.19*1.0)
        elif self.object.cust_55_act == 'C':
            table_data.append(0.19*0.5)
        elif self.object.cust_55_act == 'B':
            table_data.append(0.19*0.5)
        else: # A o nulo
            table_data.append(0.0)

        if self.object.cust_55_p1 == 'D': 
            table_data.append(0.19*1.0)
        elif self.object.cust_55_p1 == 'C':
            table_data.append(0.19*0.5)
        elif self.object.cust_55_p1 == 'B':
            table_data.append(0.19*0.5)
        else: # A o nulo
            table_data.append(0.0)
  
        if self.object.cust_55_p2 == 'D': 
            table_data.append(0.19*1.0)
        elif self.object.cust_55_p2 == 'C':
            table_data.append(0.19*0.5)
        elif self.object.cust_55_p2 == 'B':
            table_data.append(0.19*0.5)
        else: # A o nulo
            table_data.append(0.0)

        return table_data
    
    def get_table_data_vci(self):
        table_data = [] #lista vacia para almacenar resultados 
        #############VCI#################
       #vci 1.1
        if self.object.vci_11_act == 'D': 
            table_data.append(0.15*1.0)
        elif self.object.vci_11_act == 'C':
            table_data.append(0.15*0.7)
        elif self.object.vci_11_act == 'B':
            table_data.append(0.15*0.5)
        else: # A o nulo
            table_data.append(0.0)

        if self.object.vci_11_p1 == 'D': 
            table_data.append(0.15*1.0)
        elif self.object.vci_11_p1 == 'C':
            table_data.append(0.15*0.7)
        elif self.object.vci_11_p1 == 'B':
            table_data.append(0.15*0.5)
        else: # A o nulo
            table_data.append(0.0)
  
        if self.object.vci_11_p2 == 'D': 
            table_data.append(0.15*1.0)
        elif self.object.vci_11_p2 == 'C':
            table_data.append(0.15*0.7)
        elif self.object.vci_11_p2 == 'B':
            table_data.append(0.15*0.5)
        else: # A o nulo
            table_data.append(0.0)
        #vci 1.2
        if self.object.vci_12_act == 'D': 
            table_data.append(0.2*1.0)
        elif self.object.vci_12_act == 'C':
            table_data.append(0.2*0.7)
        elif self.object.vci_12_act == 'B':
            table_data.append(0.2*0.5)
        else: # A o nulo
            table_data.append(0.0)

        if self.object.vci_12_p1 == 'D': 
            table_data.append(0.2*1.0)
        elif self.object.vci_12_p1 == 'C':
            table_data.append(0.2*0.7)
        elif self.object.vci_12_p1 == 'B':
            table_data.append(0.2*0.5)
        else: # A o nulo
            table_data.append(0.0)
  
        if self.object.vci_12_p2 == 'D': 
            table_data.append(0.2*1.0)
        elif self.object.vci_12_p2 == 'C':
            table_data.append(0.2*0.7)
        elif self.object.vci_12_p2 == 'B':
            table_data.append(0.2*0.5)
        else: # A o nulo
            table_data.append(0.0)
        #vci 1.3
        if self.object.vci_13_act == 'D': 
            table_data.append(0.2*1.0)
        elif self.object.vci_13_act == 'C':
            table_data.append(0.2*0.7)
        elif self.object.vci_13_act == 'B':
            table_data.append(0.2*0.5)
        else: # A o nulo
            table_data.append(0.0)

        if self.object.vci_13_p1 == 'D': 
            table_data.append(0.2*1.0)
        elif self.object.vci_13_p1 == 'C':
            table_data.append(0.2*0.7)
        elif self.object.vci_13_p1 == 'B':
            table_data.append(0.2*0.5)
        else: # A o nulo
            table_data.append(0.0)
  
        if self.object.vci_13_p2 == 'D': 
            table_data.append(0.2*1.0)
        elif self.object.vci_13_p2 == 'C':
            table_data.append(0.2*0.7)
        elif self.object.vci_13_p2 == 'B':
            table_data.append(0.2*0.5)
        else: # A o nulo
            table_data.append(0.0)
        #vci 1.4
        if self.object.vci_14_act == 'D': 
            table_data.append(0.3*1.0)
        elif self.object.vci_14_act == 'C':
            table_data.append(0.3*0.7)
        elif self.object.vci_14_act == 'B':
            table_data.append(0.3*0.3)
        else: # A o nulo
            table_data.append(0.0)

        if self.object.vci_14_p1 == 'D': 
            table_data.append(0.3*1.0)
        elif self.object.vci_14_p1 == 'C':
            table_data.append(0.3*0.7)
        elif self.object.vci_14_p1 == 'B':
            table_data.append(0.3*0.3)
        else: # A o nulo
            table_data.append(0.0)
  
        if self.object.vci_14_p2 == 'D': 
            table_data.append(0.3*1.0)
        elif self.object.vci_14_p2 == 'C':
            table_data.append(0.3*0.7)
        elif self.object.vci_14_p2 == 'B':
            table_data.append(0.3*0.3)
        else: # A o nulo
            table_data.append(0.0)
        #vci 1.5
        if self.object.vci_15_act == 'D': 
            table_data.append(0.15*1.0)
        elif self.object.vci_15_act == 'C':
            table_data.append(0.15*0.7)
        elif self.object.vci_15_act == 'B':
            table_data.append(0.15*0.5)
        else: # A o nulo
            table_data.append(0.0)

        if self.object.vci_15_p1 == 'D': 
            table_data.append(0.15*1.0)
        elif self.object.vci_15_p1 == 'C':
            table_data.append(0.15*0.7)
        elif self.object.vci_15_p1 == 'B':
            table_data.append(0.15*0.5)
        else: # A o nulo
            table_data.append(0.0)
  
        if self.object.vci_15_p2 == 'D': 
            table_data.append(0.15*1.0)
        elif self.object.vci_15_p2 == 'C':
            table_data.append(0.15*0.7)
        elif self.object.vci_15_p2 == 'B':
            table_data.append(0.15*0.5)
        else: # A o nulo
            table_data.append(0.0)
       #vci 2.1
        if self.object.vci_21_act == 'E': 
            table_data.append(0.25*1.0)
        elif self.object.vci_21_act == 'D':
            table_data.append(0.25*0.7)
        elif self.object.vci_21_act == 'C':
            table_data.append(0.25*0.5)
        elif self.object.vci_21_act == 'B':
            table_data.append(0.25*0.3)
        else: # A o nulo
            table_data.append(0.0)

        if self.object.vci_21_p1 == 'E': 
            table_data.append(0.25*1.0)
        elif self.object.vci_21_p1 == 'D':
            table_data.append(0.25*0.7)
        elif self.object.vci_21_p1 == 'C':
            table_data.append(0.25*0.5)
        elif self.object.vci_21_p1 == 'B':
            table_data.append(0.25*0.3)
        else: # A o nulo
            table_data.append(0.0)
  
        if self.object.vci_21_p2 == 'E': 
            table_data.append(0.25*1.0)
        elif self.object.vci_21_p2 == 'D':
            table_data.append(0.25*0.7)
        elif self.object.vci_21_p2 == 'C':
            table_data.append(0.25*0.5)
        elif self.object.vci_21_p2 == 'B':
            table_data.append(0.25*0.3)
        else: # A o nulo
            table_data.append(0.0)
        #vci 2.2
        if self.object.vci_22_act == 'D': 
            table_data.append(0.25*1.0)
        elif self.object.vci_22_act == 'C':
            table_data.append(0.25*0.5)
        elif self.object.vci_22_act == 'B':
            table_data.append(0.25*0.3)
        else: # A o nulo
            table_data.append(0.0)

        if self.object.vci_22_p1 == 'D': 
            table_data.append(0.25*1.0)
        elif self.object.vci_22_p1 == 'C':
            table_data.append(0.25*0.5)
        elif self.object.vci_22_p1 == 'B':
            table_data.append(0.25*0.3)
        else: # A o nulo
            table_data.append(0.0)
  
        if self.object.vci_22_p2 == 'D': 
            table_data.append(0.25*1.0)
        elif self.object.vci_22_p2 == 'C':
            table_data.append(0.25*0.5)
        elif self.object.vci_22_p2 == 'B':
            table_data.append(0.25*0.3)
        else: # A o nulo
            table_data.append(0.0)
       #vci 2.3
        if self.object.vci_23_act == 'E': 
            table_data.append(0.3*1.0)
        elif self.object.vci_23_act == 'D':
            table_data.append(0.3*0.7)
        elif self.object.vci_23_act == 'C':
            table_data.append(0.3*0.5)
        elif self.object.vci_23_act == 'B':
            table_data.append(0.3*0.3)
        else: # A o nulo
            table_data.append(0.0)

        if self.object.vci_23_p1 == 'E': 
            table_data.append(0.3*1.0)
        elif self.object.vci_23_p1 == 'D':
            table_data.append(0.3*0.7)
        elif self.object.vci_23_p1 == 'C':
            table_data.append(0.3*0.5)
        elif self.object.vci_23_p1 == 'B':
            table_data.append(0.3*0.3)
        else: # A o nulo
            table_data.append(0.0)
  
        if self.object.vci_23_p2 == 'E': 
            table_data.append(0.3*1.0)
        elif self.object.vci_23_p2 == 'D':
            table_data.append(0.3*0.7)
        elif self.object.vci_23_p2 == 'C':
            table_data.append(0.3*0.5)
        elif self.object.vci_23_p2 == 'B':
            table_data.append(0.3*0.3)
        else: # A o nulo
            table_data.append(0.0)
       #vci 2.4
        if self.object.vci_24_act == 'E': 
            table_data.append(0.2*1.0)
        elif self.object.vci_24_act == 'D':
            table_data.append(0.2*0.7)
        elif self.object.vci_24_act == 'C':
            table_data.append(0.2*0.5)
        elif self.object.vci_24_act == 'B':
            table_data.append(0.2*0.3)
        else: # A o nulo
            table_data.append(0.0)

        if self.object.vci_24_p1 == 'E': 
            table_data.append(0.2*1.0)
        elif self.object.vci_24_p1 == 'D':
            table_data.append(0.2*0.7)
        elif self.object.vci_24_p1 == 'C':
            table_data.append(0.2*0.5)
        elif self.object.vci_24_p1 == 'B':
            table_data.append(0.2*0.3)
        else: # A o nulo
            table_data.append(0.0)
  
        if self.object.vci_24_p2 == 'E': 
            table_data.append(0.2*1.0)
        elif self.object.vci_24_p2 == 'D':
            table_data.append(0.2*0.7)
        elif self.object.vci_24_p2 == 'C':
            table_data.append(0.2*0.5)
        elif self.object.vci_24_p2 == 'B':
            table_data.append(0.2*0.3)
        else: # A o nulo
            table_data.append(0.0)
       #vci 3.1
        if self.object.vci_31_act == 'E': 
            table_data.append(0.3*1.0)
        elif self.object.vci_31_act == 'D':
            table_data.append(0.3*0.7)
        elif self.object.vci_31_act == 'C':
            table_data.append(0.3*0.5)
        elif self.object.vci_31_act == 'B':
            table_data.append(0.3*0.3)
        else: # A o nulo
            table_data.append(0.0)

        if self.object.vci_31_p1 == 'E': 
            table_data.append(0.3*1.0)
        elif self.object.vci_31_p1 == 'D':
            table_data.append(0.3*0.7)
        elif self.object.vci_31_p1 == 'C':
            table_data.append(0.3*0.5)
        elif self.object.vci_31_p1 == 'B':
            table_data.append(0.3*0.3)
        else: # A o nulo
            table_data.append(0.0)
  
        if self.object.vci_31_p2 == 'E': 
            table_data.append(0.3*1.0)
        elif self.object.vci_31_p2 == 'D':
            table_data.append(0.3*0.7)
        elif self.object.vci_31_p2 == 'C':
            table_data.append(0.3*0.5)
        elif self.object.vci_31_p2 == 'B':
            table_data.append(0.3*0.3)
        else: # A o nulo
            table_data.append(0.0)
       #vci 3.2
        if self.object.vci_32_act == 'E': 
            table_data.append(0.25*1.0)
        elif self.object.vci_32_act == 'D':
            table_data.append(0.25*0.7)
        elif self.object.vci_32_act == 'C':
            table_data.append(0.25*0.5)
        elif self.object.vci_32_act == 'B':
            table_data.append(0.25*0.3)
        else: # A o nulo
            table_data.append(0.0)

        if self.object.vci_32_p1 == 'E': 
            table_data.append(0.25*1.0)
        elif self.object.vci_32_p1 == 'D':
            table_data.append(0.25*0.7)
        elif self.object.vci_32_p1 == 'C':
            table_data.append(0.25*0.5)
        elif self.object.vci_32_p1 == 'B':
            table_data.append(0.25*0.3)
        else: # A o nulo
            table_data.append(0.0)
  
        if self.object.vci_32_p2 == 'E': 
            table_data.append(0.25*1.0)
        elif self.object.vci_32_p2 == 'D':
            table_data.append(0.25*0.7)
        elif self.object.vci_32_p2 == 'C':
            table_data.append(0.25*0.5)
        elif self.object.vci_32_p2 == 'B':
            table_data.append(0.25*0.3)
        else: # A o nulo
            table_data.append(0.0)
       #vci 3.3
        if self.object.vci_33_act == 'E': 
            table_data.append(0.3*1.0)
        elif self.object.vci_33_act == 'D':
            table_data.append(0.3*0.7)
        elif self.object.vci_33_act == 'C':
            table_data.append(0.3*0.5)
        elif self.object.vci_33_act == 'B':
            table_data.append(0.3*0.3)
        else: # A o nulo
            table_data.append(0.0)

        if self.object.vci_33_p1 == 'E': 
            table_data.append(0.3*1.0)
        elif self.object.vci_33_p1 == 'D':
            table_data.append(0.3*0.7)
        elif self.object.vci_33_p1 == 'C':
            table_data.append(0.3*0.5)
        elif self.object.vci_33_p1 == 'B':
            table_data.append(0.3*0.3)
        else: # A o nulo
            table_data.append(0.0)
  
        if self.object.vci_33_p2 == 'E': 
            table_data.append(0.3*1.0)
        elif self.object.vci_33_p2 == 'D':
            table_data.append(0.3*0.7)
        elif self.object.vci_33_p2 == 'C':
            table_data.append(0.3*0.5)
        elif self.object.vci_33_p2 == 'B':
            table_data.append(0.3*0.3)
        else: # A o nulo
            table_data.append(0.0)
       #vci 3.4
        if self.object.vci_34_act == 'E': 
            table_data.append(0.15*1.0)
        elif self.object.vci_34_act == 'D':
            table_data.append(0.15*0.7)
        elif self.object.vci_34_act == 'C':
            table_data.append(0.15*0.5)
        elif self.object.vci_34_act == 'B':
            table_data.append(0.15*0.3)
        else: # A o nulo
            table_data.append(0.0)

        if self.object.vci_34_p1 == 'E': 
            table_data.append(0.15*1.0)
        elif self.object.vci_34_p1 == 'D':
            table_data.append(0.15*0.7)
        elif self.object.vci_34_p1 == 'C':
            table_data.append(0.15*0.5)
        elif self.object.vci_34_p1 == 'B':
            table_data.append(0.15*0.3)
        else: # A o nulo
            table_data.append(0.0)
  
        if self.object.vci_34_p2 == 'E': 
            table_data.append(0.15*1.0)
        elif self.object.vci_34_p2 == 'D':
            table_data.append(0.15*0.7)
        elif self.object.vci_34_p2 == 'C':
            table_data.append(0.15*0.5)
        elif self.object.vci_34_p2 == 'B':
            table_data.append(0.15*0.3)
        else: # A o nulo
            table_data.append(0.0)
       #vci 4.1
        if self.object.vci_41_act == 'E': 
            table_data.append(0.25*1.0)
        elif self.object.vci_41_act == 'D':
            table_data.append(0.25*0.7)
        elif self.object.vci_41_act == 'C':
            table_data.append(0.25*0.5)
        elif self.object.vci_41_act == 'B':
            table_data.append(0.25*0.3)
        else: # A o nulo
            table_data.append(0.0)

        if self.object.vci_41_p1 == 'E': 
            table_data.append(0.25*1.0)
        elif self.object.vci_41_p1 == 'D':
            table_data.append(0.25*0.7)
        elif self.object.vci_41_p1 == 'C':
            table_data.append(0.25*0.5)
        elif self.object.vci_41_p1 == 'B':
            table_data.append(0.25*0.3)
        else: # A o nulo
            table_data.append(0.0)
  
        if self.object.vci_41_p2 == 'E': 
            table_data.append(0.25*1.0)
        elif self.object.vci_41_p2 == 'D':
            table_data.append(0.25*0.7)
        elif self.object.vci_41_p2 == 'C':
            table_data.append(0.25*0.5)
        elif self.object.vci_41_p2 == 'B':
            table_data.append(0.25*0.3)
        else: # A o nulo
            table_data.append(0.0)
       #vci 4.2
        if self.object.vci_42_act == 'E': 
            table_data.append(0.25*1.0)
        elif self.object.vci_42_act == 'D':
            table_data.append(0.25*0.7)
        elif self.object.vci_42_act == 'C':
            table_data.append(0.25*0.5)
        elif self.object.vci_42_act == 'B':
            table_data.append(0.25*0.3)
        else: # A o nulo
            table_data.append(0.0)

        if self.object.vci_42_p1 == 'E': 
            table_data.append(0.25*1.0)
        elif self.object.vci_42_p1 == 'D':
            table_data.append(0.25*0.7)
        elif self.object.vci_42_p1 == 'C':
            table_data.append(0.25*0.5)
        elif self.object.vci_42_p1 == 'B':
            table_data.append(0.25*0.3)
        else: # A o nulo
            table_data.append(0.0)
  
        if self.object.vci_42_p2 == 'E': 
            table_data.append(0.25*1.0)
        elif self.object.vci_42_p2 == 'D':
            table_data.append(0.25*0.7)
        elif self.object.vci_42_p2 == 'C':
            table_data.append(0.25*0.5)
        elif self.object.vci_42_p2 == 'B':
            table_data.append(0.25*0.3)
        else: # A o nulo
            table_data.append(0.0)
        #vci 4.3
        if self.object.vci_43_act == 'F': 
            table_data.append(0.25*1.0)
        elif self.object.vci_43_act == 'E':
            table_data.append(0.25*0.7)
        elif self.object.vci_43_act == 'D':
            table_data.append(0.25*0.5)
        elif self.object.vci_43_act == 'C':
            table_data.append(0.25*0.3)
        elif self.object.vci_43_act == 'B':
            table_data.append(0.25*0.3)
        else: # A o nulo
            table_data.append(0.0)

        if self.object.vci_43_p1 == 'F': 
            table_data.append(0.25*1.0)
        elif self.object.vci_43_p1 == 'E':
            table_data.append(0.25*0.7)
        elif self.object.vci_43_p1 == 'D':
            table_data.append(0.25*0.5)
        elif self.object.vci_43_p1 == 'C':
            table_data.append(0.25*0.3)
        elif self.object.vci_43_p1 == 'B':
            table_data.append(0.25*0.3)
        else: # A o nulo
            table_data.append(0.0)
  
        if self.object.vci_43_p2 == 'F': 
            table_data.append(0.25*1.0)
        elif self.object.vci_43_p2 == 'E':
            table_data.append(0.25*0.7)
        elif self.object.vci_43_p2 == 'D':
            table_data.append(0.25*0.5)
        elif self.object.vci_43_p2 == 'C':
            table_data.append(0.25*0.3)
        elif self.object.vci_43_p2 == 'B':
            table_data.append(0.25*0.3)
        else: # A o nulo
            table_data.append(0.0)
        #vci 4.4
        if self.object.vci_44_act == 'F': 
            table_data.append(0.25*1.0)
        elif self.object.vci_44_act == 'E':
            table_data.append(0.25*0.7)
        elif self.object.vci_44_act == 'D':
            table_data.append(0.25*0.5)
        elif self.object.vci_44_act == 'C':
            table_data.append(0.25*0.3)
        elif self.object.vci_44_act == 'B':
            table_data.append(0.25*0.3)
        else: # A o nulo
            table_data.append(0.0)

        if self.object.vci_44_p1 == 'F': 
            table_data.append(0.25*1.0)
        elif self.object.vci_44_p1 == 'E':
            table_data.append(0.25*0.7)
        elif self.object.vci_44_p1 == 'D':
            table_data.append(0.25*0.5)
        elif self.object.vci_44_p1 == 'C':
            table_data.append(0.25*0.3)
        elif self.object.vci_44_p1 == 'B':
            table_data.append(0.25*0.3)
        else: # A o nulo
            table_data.append(0.0)
  
        if self.object.vci_44_p2 == 'F': 
            table_data.append(0.25*1.0)
        elif self.object.vci_44_p2 == 'E':
            table_data.append(0.25*0.7)
        elif self.object.vci_44_p2 == 'D':
            table_data.append(0.25*0.5)
        elif self.object.vci_44_p2 == 'C':
            table_data.append(0.25*0.3)
        elif self.object.vci_44_p2 == 'B':
            table_data.append(0.25*0.3)
        else: # A o nulo
            table_data.append(0.0)
       #vci 5.1
        if self.object.vci_51_act == 'E': 
            table_data.append(0.33*1.0)
        elif self.object.vci_51_act == 'D':
            table_data.append(0.33*0.7)
        elif self.object.vci_51_act == 'C':
            table_data.append(0.33*0.5)
        elif self.object.vci_51_act == 'B':
            table_data.append(0.33*0.3)
        else: # A o nulo
            table_data.append(0.0)

        if self.object.vci_51_p1 == 'E': 
            table_data.append(0.33*1.0)
        elif self.object.vci_51_p1 == 'D':
            table_data.append(0.33*0.7)
        elif self.object.vci_51_p1 == 'C':
            table_data.append(0.33*0.5)
        elif self.object.vci_51_p1 == 'B':
            table_data.append(0.33*0.3)
        else: # A o nulo
            table_data.append(0.0)
  
        if self.object.vci_51_p2 == 'E': 
            table_data.append(0.33*1.0)
        elif self.object.vci_51_p2 == 'D':
            table_data.append(0.33*0.7)
        elif self.object.vci_51_p2 == 'C':
            table_data.append(0.33*0.5)
        elif self.object.vci_51_p2 == 'B':
            table_data.append(0.33*0.3)
        else: # A o nulo
            table_data.append(0.0)
        #vci 5.2
        if self.object.vci_52_act == 'F': 
            table_data.append(0.33*1.0)
        elif self.object.vci_52_act == 'E':
            table_data.append(0.33*0.7)
        elif self.object.vci_52_act == 'D':
            table_data.append(0.33*0.5)
        elif self.object.vci_52_act == 'C':
            table_data.append(0.33*0.3)
        elif self.object.vci_52_act == 'B':
            table_data.append(0.33*0.3)
        else: # A o nulo
            table_data.append(0.0)

        if self.object.vci_52_p1 == 'F': 
            table_data.append(0.33*1.0)
        elif self.object.vci_52_p1 == 'E':
            table_data.append(0.33*0.7)
        elif self.object.vci_52_p1 == 'D':
            table_data.append(0.33*0.5)
        elif self.object.vci_52_p1 == 'C':
            table_data.append(0.33*0.3)
        elif self.object.vci_52_p1 == 'B':
            table_data.append(0.33*0.3)
        else: # A o nulo
            table_data.append(0.0)
  
        if self.object.vci_52_p2 == 'F': 
            table_data.append(0.33*1.0)
        elif self.object.vci_52_p2 == 'E':
            table_data.append(0.33*0.7)
        elif self.object.vci_52_p2 == 'D':
            table_data.append(0.33*0.5)
        elif self.object.vci_52_p2 == 'C':
            table_data.append(0.33*0.3)
        elif self.object.vci_52_p2 == 'B':
            table_data.append(0.33*0.3)
        else: # A o nulo
            table_data.append(0.0)
        if self.object.vci_53_act == 'D': 
            table_data.append(0.34*1.0)
        elif self.object.vci_53_act == 'C':
            table_data.append(0.34*0.5)
        elif self.object.vci_53_act == 'B':
            table_data.append(0.34*0.3)
        else: # A o nulo
            table_data.append(0.0)

        if self.object.vci_53_p1 == 'D': 
            table_data.append(0.34*1.0)
        elif self.object.vci_53_p1 == 'C':
            table_data.append(0.34*0.5)
        elif self.object.vci_53_p1 == 'B':
            table_data.append(0.34*0.3)
        else: # A o nulo
            table_data.append(0.0)
  
        if self.object.vci_53_p2 == 'D': 
            table_data.append(0.34*1.0)
        elif self.object.vci_53_p2 == 'C':
            table_data.append(0.34*0.5)
        elif self.object.vci_53_p2 == 'B':
            table_data.append(0.34*0.3)
        else: # A o nulo
            table_data.append(0.0)

        return table_data

    def get_table_data_se(self):
        table_data = [] #lista vacia para almacenar resultados 
        #############SE#################
        #se 1.1
        if self.object.se_11_act == 'D': 
            table_data.append(0.4*1.0)
        elif self.object.se_11_act == 'C':
            table_data.append(0.4*0.7)
        elif self.object.se_11_act == 'B':
            table_data.append(0.4*0.5)
        else: # A o nulo
            table_data.append(0.0)

        if self.object.se_11_p1 == 'D': 
            table_data.append(0.4*1.0)
        elif self.object.se_11_p1 == 'C':
            table_data.append(0.4*0.7)
        elif self.object.se_11_p1 == 'B':
            table_data.append(0.4*0.5)
        else: # A o nulo
            table_data.append(0.0)
  
        if self.object.se_11_p2 == 'D': 
            table_data.append(0.4*1.0)
        elif self.object.se_11_p2 == 'C':
            table_data.append(0.4*0.7)
        elif self.object.se_11_p2 == 'B':
            table_data.append(0.4*0.5)
        else: # A o nulo
            table_data.append(0.0)
       #se 1.2
        if self.object.se_12_act == 'E': 
            table_data.append(0.25*1.0)
        elif self.object.se_12_act == 'D':
            table_data.append(0.25*0.8)
        elif self.object.se_12_act == 'C':
            table_data.append(0.25*0.65)
        elif self.object.se_12_act == 'B':
            table_data.append(0.25*0.5)
        else: # A o nulo
            table_data.append(0.0)

        if self.object.se_12_p1 == 'E': 
            table_data.append(0.25*1.0)
        elif self.object.se_12_p1 == 'D':
            table_data.append(0.25*0.8)
        elif self.object.se_12_p1 == 'C':
            table_data.append(0.25*0.65)
        elif self.object.se_12_p1 == 'B':
            table_data.append(0.25*0.5)
        else: # A o nulo
            table_data.append(0.0)
  
        if self.object.se_12_p2 == 'E': 
            table_data.append(0.25*1.0)
        elif self.object.se_12_p2 == 'D':
            table_data.append(0.25*0.8)
        elif self.object.se_12_p2 == 'C':
            table_data.append(0.25*0.65)
        elif self.object.se_12_p2 == 'B':
            table_data.append(0.25*0.5)
        else: # A o nulo
            table_data.append(0.0)
        #se 1.3
        if self.object.se_13_act == 'D': 
            table_data.append(0.25*1.0)
        elif self.object.se_13_act == 'C':
            table_data.append(0.25*0.7)
        elif self.object.se_13_act == 'B':
            table_data.append(0.25*0.5)
        else: # A o nulo
            table_data.append(0.0)

        if self.object.se_13_p1 == 'D': 
            table_data.append(0.25*1.0)
        elif self.object.se_13_p1 == 'C':
            table_data.append(0.25*0.7)
        elif self.object.se_13_p1 == 'B':
            table_data.append(0.25*0.5)
        else: # A o nulo
            table_data.append(0.0)
  
        if self.object.se_13_p2 == 'D': 
            table_data.append(0.25*1.0)
        elif self.object.se_13_p2 == 'C':
            table_data.append(0.25*0.7)
        elif self.object.se_13_p2 == 'B':
            table_data.append(0.25*0.5)
        else: # A o nulo
            table_data.append(0.0)
        #se 1.4
        if self.object.se_14_act == 'D': 
            table_data.append(0.1*1.0)
        elif self.object.se_14_act == 'C':
            table_data.append(0.1*0.7)
        elif self.object.se_14_act == 'B':
            table_data.append(0.1*0.5)
        else: # A o nulo
            table_data.append(0.0)

        if self.object.se_14_p1 == 'D': 
            table_data.append(0.1*1.0)
        elif self.object.se_14_p1 == 'C':
            table_data.append(0.1*0.7)
        elif self.object.se_14_p1 == 'B':
            table_data.append(0.1*0.5)
        else: # A o nulo
            table_data.append(0.0)
  
        if self.object.se_14_p2 == 'D': 
            table_data.append(0.1*1.0)
        elif self.object.se_14_p2 == 'C':
            table_data.append(0.1*0.7)
        elif self.object.se_14_p2 == 'B':
            table_data.append(0.1*0.5)
        else: # A o nulo
            table_data.append(0.0)
        #se 2.1
        if self.object.se_21_act == 'D': 
            table_data.append(0.2*1.0)
        elif self.object.se_21_act == 'C':
            table_data.append(0.2*0.5)
        elif self.object.se_21_act == 'B':
            table_data.append(0.2*0.3)
        else: # A o nulo
            table_data.append(0.0)

        if self.object.se_21_p1 == 'D': 
            table_data.append(0.2*1.0)
        elif self.object.se_21_p1 == 'C':
            table_data.append(0.2*0.5)
        elif self.object.se_21_p1 == 'B':
            table_data.append(0.2*0.3)
        else: # A o nulo
            table_data.append(0.0)
  
        if self.object.se_21_p2 == 'D': 
            table_data.append(0.2*1.0)
        elif self.object.se_21_p2 == 'C':
            table_data.append(0.2*0.5)
        elif self.object.se_21_p2 == 'B':
            table_data.append(0.2*0.3)
        else: # A o nulo
            table_data.append(0.0)
       #se 2.2
        if self.object.se_22_act == 'E': 
            table_data.append(0.25*1.0)
        elif self.object.se_22_act == 'D':
            table_data.append(0.25*0.7)
        elif self.object.se_22_act == 'C':
            table_data.append(0.25*0.5)
        elif self.object.se_22_act == 'B':
            table_data.append(0.25*0.3)
        else: # A o nulo
            table_data.append(0.0)

        if self.object.se_22_p1 == 'E': 
            table_data.append(0.25*1.0)
        elif self.object.se_22_p1 == 'D':
            table_data.append(0.25*0.7)
        elif self.object.se_22_p1 == 'C':
            table_data.append(0.25*0.5)
        elif self.object.se_22_p1 == 'B':
            table_data.append(0.25*0.3)
        else: # A o nulo
            table_data.append(0.0)
  
        if self.object.se_22_p2 == 'E': 
            table_data.append(0.25*1.0)
        elif self.object.se_22_p2 == 'D':
            table_data.append(0.25*0.7)
        elif self.object.se_22_p2 == 'C':
            table_data.append(0.25*0.5)
        elif self.object.se_22_p2 == 'B':
            table_data.append(0.25*0.3)
        else: # A o nulo
            table_data.append(0.0)
        #se 2.3
        if self.object.se_23_act == 'D': 
            table_data.append(0.2*1.0)
        elif self.object.se_23_act == 'C':
            table_data.append(0.2*0.5)
        elif self.object.se_23_act == 'B':
            table_data.append(0.2*0.3)
        else: # A o nulo
            table_data.append(0.0)

        if self.object.se_23_p1 == 'D': 
            table_data.append(0.2*1.0)
        elif self.object.se_23_p1 == 'C':
            table_data.append(0.2*0.5)
        elif self.object.se_23_p1 == 'B':
            table_data.append(0.2*0.3)
        else: # A o nulo
            table_data.append(0.0)
  
        if self.object.se_23_p2 == 'D': 
            table_data.append(0.2*1.0)
        elif self.object.se_23_p2 == 'C':
            table_data.append(0.2*0.5)
        elif self.object.se_23_p2 == 'B':
            table_data.append(0.2*0.3)
        else: # A o nulo
            table_data.append(0.0)
        #se 2.4
        if self.object.se_24_act == 'D': 
            table_data.append(0.18*1.0)
        elif self.object.se_24_act == 'C':
            table_data.append(0.18*0.7)
        elif self.object.se_24_act == 'B':
            table_data.append(0.18*0.3)
        else: # A o nulo
            table_data.append(0.0)

        if self.object.se_24_p1 == 'D': 
            table_data.append(0.18*1.0)
        elif self.object.se_24_p1 == 'C':
            table_data.append(0.18*0.7)
        elif self.object.se_24_p1 == 'B':
            table_data.append(0.18*0.3)
        else: # A o nulo
            table_data.append(0.0)
  
        if self.object.se_24_p2 == 'D': 
            table_data.append(0.18*1.0)
        elif self.object.se_24_p2 == 'C':
            table_data.append(0.18*0.7)
        elif self.object.se_24_p2 == 'B':
            table_data.append(0.18*0.3)
        else: # A o nulo
            table_data.append(0.0)
        #se 2.5
        if self.object.se_25_act == 'D': 
            table_data.append(0.17*1.0)
        elif self.object.se_25_act == 'C':
            table_data.append(0.17*0.7)
        elif self.object.se_25_act == 'B':
            table_data.append(0.17*0.3)
        else: # A o nulo
            table_data.append(0.0)

        if self.object.se_25_p1 == 'D': 
            table_data.append(0.17*1.0)
        elif self.object.se_25_p1 == 'C':
            table_data.append(0.17*0.7)
        elif self.object.se_25_p1 == 'B':
            table_data.append(0.17*0.3)
        else: # A o nulo
            table_data.append(0.0)
  
        if self.object.se_25_p2 == 'D': 
            table_data.append(0.17*1.0)
        elif self.object.se_25_p2 == 'C':
            table_data.append(0.17*0.7)
        elif self.object.se_25_p2 == 'B':
            table_data.append(0.17*0.3)
        else: # A o nulo
            table_data.append(0.0)
       #se 3.1
        if self.object.se_31_act == 'E': 
            table_data.append(0.25*1.0)
        elif self.object.se_31_act == 'D':
            table_data.append(0.25*0.7)
        elif self.object.se_31_act == 'C':
            table_data.append(0.25*0.5)
        elif self.object.se_31_act == 'B':
            table_data.append(0.25*0.3)
        else: # A o nulo
            table_data.append(0.0)

        if self.object.se_31_p1 == 'E': 
            table_data.append(0.25*1.0)
        elif self.object.se_31_p1 == 'D':
            table_data.append(0.25*0.7)
        elif self.object.se_31_p1 == 'C':
            table_data.append(0.25*0.5)
        elif self.object.se_31_p1 == 'B':
            table_data.append(0.25*0.3)
        else: # A o nulo
            table_data.append(0.0)
  
        if self.object.se_31_p2 == 'E': 
            table_data.append(0.25*1.0)
        elif self.object.se_31_p2 == 'D':
            table_data.append(0.25*0.7)
        elif self.object.se_31_p2 == 'C':
            table_data.append(0.25*0.5)
        elif self.object.se_31_p2 == 'B':
            table_data.append(0.25*0.3)
        else: # A o nulo
            table_data.append(0.0)
       #se 3.2
        if self.object.se_32_act == 'E': 
            table_data.append(0.25*1.0)
        elif self.object.se_32_act == 'D':
            table_data.append(0.25*0.7)
        elif self.object.se_32_act == 'C':
            table_data.append(0.25*0.3)
        elif self.object.se_32_act == 'B':
            table_data.append(0.25*0.1)
        else: # A o nulo
            table_data.append(0.0)

        if self.object.se_32_p1 == 'E': 
            table_data.append(0.25*1.0)
        elif self.object.se_32_p1 == 'D':
            table_data.append(0.25*0.7)
        elif self.object.se_32_p1 == 'C':
            table_data.append(0.25*0.3)
        elif self.object.se_32_p1 == 'B':
            table_data.append(0.25*0.1)
        else: # A o nulo
            table_data.append(0.0)
  
        if self.object.se_32_p2 == 'E': 
            table_data.append(0.25*1.0)
        elif self.object.se_32_p2 == 'D':
            table_data.append(0.25*0.7)
        elif self.object.se_32_p2 == 'C':
            table_data.append(0.25*0.3)
        elif self.object.se_32_p2 == 'B':
            table_data.append(0.25*0.1)
        else: # A o nulo
            table_data.append(0.0)
       #se 3.3
        if self.object.se_33_act == 'E': 
            table_data.append(0.25*1.0)
        elif self.object.se_33_act == 'D':
            table_data.append(0.25*0.7)
        elif self.object.se_33_act == 'C':
            table_data.append(0.25*0.3)
        elif self.object.se_33_act == 'B':
            table_data.append(0.25*0.1)
        else: # A o nulo
            table_data.append(0.0)

        if self.object.se_33_p1 == 'E': 
            table_data.append(0.25*1.0)
        elif self.object.se_33_p1 == 'D':
            table_data.append(0.25*0.7)
        elif self.object.se_33_p1 == 'C':
            table_data.append(0.25*0.3)
        elif self.object.se_33_p1 == 'B':
            table_data.append(0.25*0.1)
        else: # A o nulo
            table_data.append(0.0)
  
        if self.object.se_33_p2 == 'E': 
            table_data.append(0.25*1.0)
        elif self.object.se_33_p2 == 'D':
            table_data.append(0.25*0.7)
        elif self.object.se_33_p2 == 'C':
            table_data.append(0.25*0.3)
        elif self.object.se_33_p2 == 'B':
            table_data.append(0.25*0.1)
        else: # A o nulo
            table_data.append(0.0)
        #se 3.4
        if self.object.se_34_act == 'D': 
            table_data.append(0.25*1.0)
        elif self.object.se_34_act == 'C':
            table_data.append(0.25*0.7)
        elif self.object.se_34_act == 'B':
            table_data.append(0.25*0.5)
        else: # A o nulo
            table_data.append(0.0)

        if self.object.se_34_p1 == 'D': 
            table_data.append(0.25*1.0)
        elif self.object.se_34_p1 == 'C':
            table_data.append(0.25*0.7)
        elif self.object.se_34_p1 == 'B':
            table_data.append(0.25*0.5)
        else: # A o nulo
            table_data.append(0.0)
  
        if self.object.se_34_p2 == 'D': 
            table_data.append(0.25*1.0)
        elif self.object.se_34_p2 == 'C':
            table_data.append(0.25*0.7)
        elif self.object.se_34_p2 == 'B':
            table_data.append(0.25*0.5)
        else: # A o nulo
            table_data.append(0.0)
        #se 4.1
        if self.object.se_41_act == 'D': 
            table_data.append(0.2*1.0)
        elif self.object.se_41_act == 'C':
            table_data.append(0.2*0.7)
        elif self.object.se_41_act == 'B':
            table_data.append(0.2*0.5)
        else: # A o nulo
            table_data.append(0.0)

        if self.object.se_41_p1 == 'D': 
            table_data.append(0.2*1.0)
        elif self.object.se_41_p1 == 'C':
            table_data.append(0.2*0.7)
        elif self.object.se_41_p1 == 'B':
            table_data.append(0.2*0.5)
        else: # A o nulo
            table_data.append(0.0)
  
        if self.object.se_41_p2 == 'D': 
            table_data.append(0.2*1.0)
        elif self.object.se_41_p2 == 'C':
            table_data.append(0.2*0.7)
        elif self.object.se_41_p2 == 'B':
            table_data.append(0.2*0.5)
        else: # A o nulo
            table_data.append(0.0)
        #se 4.2
        if self.object.se_42_act == 'D': 
            table_data.append(0.2*1.0)
        elif self.object.se_42_act == 'C':
            table_data.append(0.2*0.7)
        elif self.object.se_42_act == 'B':
            table_data.append(0.2*0.5)
        else: # A o nulo
            table_data.append(0.0)

        if self.object.se_42_p1 == 'D': 
            table_data.append(0.2*1.0)
        elif self.object.se_42_p1 == 'C':
            table_data.append(0.2*0.7)
        elif self.object.se_42_p1 == 'B':
            table_data.append(0.2*0.5)
        else: # A o nulo
            table_data.append(0.0)
  
        if self.object.se_42_p2 == 'D': 
            table_data.append(0.2*1.0)
        elif self.object.se_42_p2 == 'C':
            table_data.append(0.2*0.7)
        elif self.object.se_42_p2 == 'B':
            table_data.append(0.2*0.5)
        else: # A o nulo
            table_data.append(0.0)
        #se 4.3
        if self.object.se_43_act == 'D': 
            table_data.append(0.2*1.0)
        elif self.object.se_43_act == 'C':
            table_data.append(0.2*0.5)
        elif self.object.se_43_act == 'B':
            table_data.append(0.2*0.3)
        else: # A o nulo
            table_data.append(0.0)

        if self.object.se_43_p1 == 'D': 
            table_data.append(0.2*1.0)
        elif self.object.se_43_p1 == 'C':
            table_data.append(0.2*0.5)
        elif self.object.se_43_p1 == 'B':
            table_data.append(0.2*0.3)
        else: # A o nulo
            table_data.append(0.0)
  
        if self.object.se_43_p2 == 'D': 
            table_data.append(0.2*1.0)
        elif self.object.se_43_p2 == 'C':
            table_data.append(0.2*0.5)
        elif self.object.se_43_p2 == 'B':
            table_data.append(0.2*0.3)
        else: # A o nulo
            table_data.append(0.0)
       #se 4.4
        if self.object.se_44_act == 'E': 
            table_data.append(0.2*1.0)
        elif self.object.se_44_act == 'D':
            table_data.append(0.2*0.7)
        elif self.object.se_44_act == 'C':
            table_data.append(0.2*0.5)
        elif self.object.se_44_act == 'B':
            table_data.append(0.2*0.3)
        else: # A o nulo
            table_data.append(0.0)

        if self.object.se_44_p1 == 'E': 
            table_data.append(0.2*1.0)
        elif self.object.se_44_p1 == 'D':
            table_data.append(0.2*0.7)
        elif self.object.se_44_p1 == 'C':
            table_data.append(0.2*0.5)
        elif self.object.se_44_p1 == 'B':
            table_data.append(0.2*0.3)
        else: # A o nulo
            table_data.append(0.0)
  
        if self.object.se_44_p2 == 'E': 
            table_data.append(0.2*1.0)
        elif self.object.se_44_p2 == 'D':
            table_data.append(0.2*0.7)
        elif self.object.se_44_p2 == 'C':
            table_data.append(0.2*0.5)
        elif self.object.se_44_p2 == 'B':
            table_data.append(0.2*0.3)
        else: # A o nulo
            table_data.append(0.0)
       #se 4.5
        if self.object.se_45_act == 'E': 
            table_data.append(0.2*1.0)
        elif self.object.se_45_act == 'D':
            table_data.append(0.2*0.7)
        elif self.object.se_45_act == 'C':
            table_data.append(0.2*0.5)
        elif self.object.se_45_act == 'B':
            table_data.append(0.2*0.3)
        else: # A o nulo
            table_data.append(0.0)

        if self.object.se_45_p1 == 'E': 
            table_data.append(0.2*1.0)
        elif self.object.se_45_p1 == 'D':
            table_data.append(0.2*0.7)
        elif self.object.se_45_p1 == 'C':
            table_data.append(0.2*0.5)
        elif self.object.se_45_p1 == 'B':
            table_data.append(0.2*0.3)
        else: # A o nulo
            table_data.append(0.0)
  
        if self.object.se_45_p2 == 'E': 
            table_data.append(0.2*1.0)
        elif self.object.se_45_p2 == 'D':
            table_data.append(0.2*0.7)
        elif self.object.se_45_p2 == 'C':
            table_data.append(0.2*0.5)
        elif self.object.se_45_p2 == 'B':
            table_data.append(0.2*0.3)
        else: # A o nulo
            table_data.append(0.0)
        #se 5.1
        if self.object.se_51_act == 'D': 
            table_data.append(0.35*1.0)
        elif self.object.se_51_act == 'C':
            table_data.append(0.35*0.7)
        elif self.object.se_51_act == 'B':
            table_data.append(0.35*0.5)
        else: # A o nulo
            table_data.append(0.0)

        if self.object.se_51_p1 == 'D': 
            table_data.append(0.35*1.0)
        elif self.object.se_51_p1 == 'C':
            table_data.append(0.35*0.7)
        elif self.object.se_51_p1 == 'B':
            table_data.append(0.35*0.5)
        else: # A o nulo
            table_data.append(0.0)
  
        if self.object.se_51_p2 == 'D': 
            table_data.append(0.35*1.0)
        elif self.object.se_51_p2 == 'C':
            table_data.append(0.35*0.7)
        elif self.object.se_51_p2 == 'B':
            table_data.append(0.35*0.5)
        else: # A o nulo
            table_data.append(0.0)
       #se 5.2
        if self.object.se_52_act == 'E': 
            table_data.append(0.35*1.0)
        elif self.object.se_52_act == 'D':
            table_data.append(0.35*0.7)
        elif self.object.se_52_act == 'C':
            table_data.append(0.35*0.5)
        elif self.object.se_52_act == 'B':
            table_data.append(0.35*0.3)
        else: # A o nulo
            table_data.append(0.0)

        if self.object.se_52_p1 == 'E': 
            table_data.append(0.35*1.0)
        elif self.object.se_52_p1 == 'D':
            table_data.append(0.35*0.7)
        elif self.object.se_52_p1 == 'C':
            table_data.append(0.35*0.5)
        elif self.object.se_52_p1 == 'B':
            table_data.append(0.35*0.3)
        else: # A o nulo
            table_data.append(0.0)
  
        if self.object.se_52_p2 == 'E': 
            table_data.append(0.35*1.0)
        elif self.object.se_52_p2 == 'D':
            table_data.append(0.35*0.7)
        elif self.object.se_52_p2 == 'C':
            table_data.append(0.35*0.5)
        elif self.object.se_52_p2 == 'B':
            table_data.append(0.35*0.3)
        else: # A o nulo
            table_data.append(0.0)
        #se 5.3
        if self.object.se_53_act == 'D': 
            table_data.append(0.3*1.0)
        elif self.object.se_53_act == 'C':
            table_data.append(0.3*0.7)
        elif self.object.se_53_act == 'B':
            table_data.append(0.3*0.3)
        else: # A o nulo
            table_data.append(0.0)

        if self.object.se_53_p1 == 'D': 
            table_data.append(0.3*1.0)
        elif self.object.se_53_p1 == 'C':
            table_data.append(0.3*0.7)
        elif self.object.se_53_p1 == 'B':
            table_data.append(0.3*0.3)
        else: # A o nulo
            table_data.append(0.0)
  
        if self.object.se_53_p2 == 'D': 
            table_data.append(0.3*1.0)
        elif self.object.se_53_p2 == 'C':
            table_data.append(0.3*0.7)
        elif self.object.se_53_p2 == 'B':
            table_data.append(0.3*0.3)
        else: # A o nulo
            table_data.append(0.0)

        return table_data

    def sum_results(self,srm, os, go, wam, tech, cust, vci, se):
        self.data_act = []
        self.data_p1 = []
        self.data_p2 = []
        self.prom_data_act = []
        self.prom_data_p1 = []
        self.prom_data_p2 = []
        ####SRM####
        i=0
        self.data_act.append(srm[0+i]+srm[3+i]+srm[6+i])
        self.data_act.append(srm[9+i]+srm[12+i]+srm[15+i]+srm[18+i]+srm[21+i]+srm[24+i])
        self.data_act.append(srm[27+i]+srm[30+i]+srm[33+i]+srm[36+i])
        self.data_act.append(srm[39+i]+srm[42+i]+srm[45+i])
        self.data_act.append(srm[48+i]+srm[51+i]+srm[54+i])
        i=1
        self.data_p1.append(srm[0+i]+srm[3+i]+srm[6+i])
        self.data_p1.append(srm[9+i]+srm[12+i]+srm[15+i]+srm[18+i]+srm[21+i]+srm[24+i])
        self.data_p1.append(srm[27+i]+srm[30+i]+srm[33+i]+srm[36+i])
        self.data_p1.append(srm[39+i]+srm[42+i]+srm[45+i])
        self.data_p1.append(srm[48+i]+srm[51+i]+srm[54+i])
        i=2
        self.data_p2.append(srm[0+i]+srm[3+i]+srm[6+i])
        self.data_p2.append(srm[9+i]+srm[12+i]+srm[15+i]+srm[18+i]+srm[21+i]+srm[24+i])
        self.data_p2.append(srm[27+i]+srm[30+i]+srm[33+i]+srm[36+i])
        self.data_p2.append(srm[39+i]+srm[42+i]+srm[45+i])
        self.data_p2.append(srm[48+i]+srm[51+i]+srm[54+i])

                ####OS####
        i=0
        self.data_act.append(os[0+i]+os[3+i]+os[6+i])
        self.data_act.append(os[9+i]+os[12+i]+os[15+i]+os[18+i]+os[21+i])
        self.data_act.append(os[24+i]+os[27+i]+os[30+i]+os[33+i]+os[36+i]+os[39+i])
        self.data_act.append(os[42+i]+os[45+i]+os[48+i])
        self.data_act.append(os[51+i]+os[54+i]+os[57+i])
        i=1
        self.data_p1.append(os[0+i]+os[3+i]+os[6+i])
        self.data_p1.append(os[9+i]+os[12+i]+os[15+i]+os[18+i]+os[21+i])
        self.data_p1.append(os[24+i]+os[27+i]+os[30+i]+os[33+i]+os[36+i]+os[39+i])
        self.data_p1.append(os[42+i]+os[45+i]+os[48+i])
        self.data_p1.append(os[51+i]+os[54+i]+os[57+i])
        i=2
        self.data_p2.append(os[0+i]+os[3+i]+os[6+i])
        self.data_p2.append(os[9+i]+os[12+i]+os[15+i]+os[18+i]+os[21+i])
        self.data_p2.append(os[24+i]+os[27+i]+os[30+i]+os[33+i]+os[36+i]+os[39+i])
        self.data_p2.append(os[42+i]+os[45+i]+os[48+i])
        self.data_p2.append(os[51+i]+os[54+i]+os[57+i])

                ####GO####
        i=0
        self.data_act.append(go[0+i]+go[3+i]+go[6+i]+go[9+i]+go[12+i])
        self.data_act.append(go[15+i]+go[18+i]+go[21+i]+go[24+i])
        self.data_act.append(go[27+i]+go[30+i]+go[33+i]+go[36+i]+go[39+i]+go[42+i])
        self.data_act.append(go[45+i]+go[48+i]+go[51+i]+go[54+i]+go[57+i])
        self.data_act.append(go[60+i]+go[63+i])
        i=1
        self.data_p1.append(go[0+i]+go[3+i]+go[6+i]+go[9+i]+go[12+i])
        self.data_p1.append(go[15+i]+go[18+i]+go[21+i]+go[24+i])
        self.data_p1.append(go[27+i]+go[30+i]+go[33+i]+go[36+i]+go[39+i]+go[42+i])
        self.data_p1.append(go[45+i]+go[48+i]+go[51+i]+go[54+i]+go[57+i])
        self.data_p1.append(go[60+i]+go[63+i])
        i=2
        self.data_p2.append(go[0+i]+go[3+i]+go[6+i]+go[9+i]+go[12+i])
        self.data_p2.append(go[15+i]+go[18+i]+go[21+i]+go[24+i])
        self.data_p2.append(go[27+i]+go[30+i]+go[33+i]+go[36+i]+go[39+i]+go[42+i])
        self.data_p2.append(go[45+i]+go[48+i]+go[51+i]+go[54+i]+go[57+i])
        self.data_p2.append(go[60+i]+go[63+i])

                ####WAM####
        i=0
        self.data_act.append(wam[0+i]+wam[3+i]+wam[6+i])
        self.data_act.append(wam[9+i]+wam[12+i]+wam[15+i])
        self.data_act.append(wam[18+i]+wam[21+i]+wam[24+i]+wam[27+i]+wam[30+i]+wam[33+i]+wam[36+i])
        self.data_act.append(wam[39+i]+wam[42+i]+wam[45+i]+wam[48+i])
        self.data_act.append(wam[51+i]+wam[54+i])
        i=1
        self.data_p1.append(wam[0+i]+wam[3+i]+wam[6+i])
        self.data_p1.append(wam[9+i]+wam[12+i]+wam[15+i])
        self.data_p1.append(wam[18+i]+wam[21+i]+wam[24+i]+wam[27+i]+wam[30+i]+wam[33+i]+wam[36+i])
        self.data_p1.append(wam[39+i]+wam[42+i]+wam[45+i]+wam[48+i])
        self.data_p1.append(wam[51+i]+wam[54+i])
        i=2
        self.data_p2.append(wam[0+i]+wam[3+i]+wam[6+i])
        self.data_p2.append(wam[9+i]+wam[12+i]+wam[15+i])
        self.data_p2.append(wam[18+i]+wam[21+i]+wam[24+i]+wam[27+i]+wam[30+i]+wam[33+i]+wam[36+i])
        self.data_p2.append(wam[39+i]+wam[42+i]+wam[45+i]+wam[48+i])
        self.data_p2.append(wam[51+i]+wam[54+i])

                ####TECH####
        i=0
        self.data_act.append(tech[0+i]+tech[3+i]+tech[6+i]+tech[9+i]+tech[12+i])
        self.data_act.append(tech[15+i]+tech[18+i]+tech[21+i]+tech[24+i]+tech[27+i]+tech[30+i]+tech[33+i])
        self.data_act.append(tech[36+i]+tech[39+i]+tech[42+i]+tech[45+i]+tech[48+i]+tech[51+i])
        self.data_act.append(tech[54+i]+tech[54+i]+tech[57+i]+tech[60+i]+tech[63+i]+tech[66+i]+tech[69+i])
        self.data_act.append(tech[72+i]+tech[75+i])
        i=1
        self.data_p1.append(tech[0+i]+tech[3+i]+tech[6+i]+tech[9+i]+tech[12+i])
        self.data_p1.append(tech[15+i]+tech[18+i]+tech[21+i]+tech[24+i]+tech[27+i]+tech[30+i]+tech[33+i])
        self.data_p1.append(tech[36+i]+tech[39+i]+tech[42+i]+tech[45+i]+tech[48+i]+tech[51+i])
        self.data_p1.append(tech[54+i]+tech[54+i]+tech[57+i]+tech[60+i]+tech[63+i]+tech[66+i]+tech[69+i])
        self.data_p1.append(tech[72+i]+tech[75+i])
        i=2
        self.data_p2.append(tech[0+i]+tech[3+i]+tech[6+i]+tech[9+i]+tech[12+i])
        self.data_p2.append(tech[15+i]+tech[18+i]+tech[21+i]+tech[24+i]+tech[27+i]+tech[30+i]+tech[33+i])
        self.data_p2.append(tech[36+i]+tech[39+i]+tech[42+i]+tech[45+i]+tech[48+i]+tech[51+i])
        self.data_p2.append(tech[54+i]+tech[54+i]+tech[57+i]+tech[60+i]+tech[63+i]+tech[66+i]+tech[69+i])
        self.data_p2.append(tech[72+i]+tech[75+i])

                ####CUST####
        i=0
        self.data_act.append(cust[0+i]+cust[3+i]+cust[6+i]+cust[9+i])
        self.data_act.append(cust[12+i]+cust[15+i]+cust[18+i]+cust[21+i]+cust[24+i]+cust[27+i])
        self.data_act.append(cust[30+i]+cust[33+i]+cust[36+i]+cust[39+i]+cust[42+i]+cust[45+i]+cust[48+i]+cust[51+i]+cust[54+i])
        self.data_act.append(cust[57+i]+cust[60+i]+cust[63+i]+cust[66+i]+cust[69+i]+cust[72+i]+cust[75+i])
        self.data_act.append(cust[78+i]+cust[81+i]+cust[84+i]+cust[87+i]+cust[90+i])
        i=1
        self.data_p1.append(cust[0+i]+cust[3+i]+cust[6+i]+cust[9+i])
        self.data_p1.append(cust[12+i]+cust[15+i]+cust[18+i]+cust[21+i]+cust[24+i]+cust[27+i])
        self.data_p1.append(cust[30+i]+cust[33+i]+cust[36+i]+cust[39+i]+cust[42+i]+cust[45+i]+cust[48+i]+cust[51+i]+cust[54+i])
        self.data_p1.append(cust[57+i]+cust[60+i]+cust[63+i]+cust[66+i]+cust[69+i]+cust[72+i]+cust[75+i])
        self.data_p1.append(cust[78+i]+cust[81+i]+cust[84+i]+cust[87+i]+cust[90+i])
        i=2
        self.data_p2.append(cust[0+i]+cust[3+i]+cust[6+i]+cust[9+i])
        self.data_p2.append(cust[12+i]+cust[15+i]+cust[18+i]+cust[21+i]+cust[24+i]+cust[27+i])
        self.data_p2.append(cust[30+i]+cust[33+i]+cust[36+i]+cust[39+i]+cust[42+i]+cust[45+i]+cust[48+i]+cust[51+i]+cust[54+i])
        self.data_p2.append(cust[57+i]+cust[60+i]+cust[63+i]+cust[66+i]+cust[69+i]+cust[72+i]+cust[75+i])
        self.data_p2.append(cust[78+i]+cust[81+i]+cust[84+i]+cust[87+i]+cust[90+i])


                ####VCI####
        i=0
        self.data_act.append(vci[0+i]+vci[3+i]+vci[6+i]+vci[9+i]+vci[12+i])
        self.data_act.append(vci[15+i]+vci[18+i]+vci[21+i]+vci[24+i])
        self.data_act.append(vci[27+i]+vci[30+i]+vci[33+i]+vci[36+i])
        self.data_act.append(vci[39+i]+vci[42+i]+vci[45+i]+vci[48+i])
        self.data_act.append(vci[51+i]+vci[54+i]+vci[57+i])

        i=1
        self.data_p1.append(vci[0+i]+vci[3+i]+vci[6+i]+vci[9+i]+vci[12+i])
        self.data_p1.append(vci[15+i]+vci[18+i]+vci[21+i]+vci[24+i])
        self.data_p1.append(vci[27+i]+vci[30+i]+vci[33+i]+vci[36+i])
        self.data_p1.append(vci[39+i]+vci[42+i]+vci[45+i]+vci[48+i])
        self.data_p1.append(vci[51+i]+vci[54+i]+vci[57+i])

        i=2
        self.data_p2.append(vci[0+i]+vci[3+i]+vci[6+i]+vci[9+i]+vci[12+i])
        self.data_p2.append(vci[15+i]+vci[18+i]+vci[21+i]+vci[24+i])
        self.data_p2.append(vci[27+i]+vci[30+i]+vci[33+i]+vci[36+i])
        self.data_p2.append(vci[39+i]+vci[42+i]+vci[45+i]+vci[48+i])
        self.data_p2.append(vci[51+i]+vci[54+i]+vci[57+i])


                ####SE####
        i=0
        self.data_act.append(se[0+i]+se[3+i]+se[6+i]+se[9+i])
        self.data_act.append(se[12+i]+se[15+i]+se[18+i]+se[21+i]+se[24+i])
        self.data_act.append(se[27+i]+se[30+i]+se[33+i]+se[36+i])
        self.data_act.append(se[39+i]+se[42+i]+se[45+i]+se[48+i]+se[51+i])
        self.data_act.append(se[54+i]+se[57+i]+se[60+i])
        i=1
        self.data_p1.append(se[0+i]+se[3+i]+se[6+i]+se[9+i])
        self.data_p1.append(se[12+i]+se[15+i]+se[18+i]+se[21+i]+se[24+i])
        self.data_p1.append(se[27+i]+se[30+i]+se[33+i]+se[36+i])
        self.data_p1.append(se[39+i]+se[42+i]+se[45+i]+se[48+i]+se[51+i])
        self.data_p1.append(se[54+i]+se[57+i]+se[60+i])
        i=2
        self.data_p2.append(se[0+i]+se[3+i]+se[6+i]+se[9+i])
        self.data_p2.append(se[12+i]+se[15+i]+se[18+i]+se[21+i]+se[24+i])
        self.data_p2.append(se[27+i]+se[30+i]+se[33+i]+se[36+i])
        self.data_p2.append(se[39+i]+se[42+i]+se[45+i]+se[48+i]+se[51+i])
        self.data_p2.append(se[54+i]+se[57+i]+se[60+i])


        #PROMEDIOS
        self.prom_data_act.append((self.data_act[0]+self.data_act[1]+self.data_act[2]+self.data_act[3]+self.data_act[4])/5)
        self.prom_data_act.append((self.data_act[5]+self.data_act[6]+self.data_act[7]+self.data_act[8]+self.data_act[9])/5)
        self.prom_data_act.append((self.data_act[10]+self.data_act[11]+self.data_act[12]+self.data_act[13]+self.data_act[14])/5)
        self.prom_data_act.append((self.data_act[15]+self.data_act[16]+self.data_act[17]+self.data_act[18]+self.data_act[19])/5)
        self.prom_data_act.append((self.data_act[20]+self.data_act[21]+self.data_act[22]+self.data_act[23]+self.data_act[24])/5)
        self.prom_data_act.append((self.data_act[25]+self.data_act[26]+self.data_act[27]+self.data_act[28]+self.data_act[29])/5)
        self.prom_data_act.append((self.data_act[30]+self.data_act[31]+self.data_act[32]+self.data_act[33]+self.data_act[34])/5)
        self.prom_data_act.append((self.data_act[35]+self.data_act[36]+self.data_act[37]+self.data_act[38]+self.data_act[39])/5)
        self.prom_data_act.append((self.prom_data_act[0]+self.prom_data_act[1]+self.prom_data_act[2]+self.prom_data_act[3]+self.prom_data_act[4]+self.prom_data_act[5]+self.prom_data_act[6]+self.prom_data_act[7])/8)

        self.prom_data_p1.append((self.data_p1[0]+self.data_p1[1]+self.data_p1[2]+self.data_p1[3]+self.data_p1[4])/5)
        self.prom_data_p1.append((self.data_p1[5]+self.data_p1[6]+self.data_p1[7]+self.data_p1[8]+self.data_p1[9])/5)
        self.prom_data_p1.append((self.data_p1[10]+self.data_p1[11]+self.data_p1[12]+self.data_p1[13]+self.data_p1[14])/5)
        self.prom_data_p1.append((self.data_p1[15]+self.data_p1[16]+self.data_p1[17]+self.data_p1[18]+self.data_p1[19])/5)
        self.prom_data_p1.append((self.data_p1[20]+self.data_p1[21]+self.data_p1[22]+self.data_p1[23]+self.data_p1[24])/5)
        self.prom_data_p1.append((self.data_p1[25]+self.data_p1[26]+self.data_p1[27]+self.data_p1[28]+self.data_p1[29])/5)
        self.prom_data_p1.append((self.data_p1[30]+self.data_p1[31]+self.data_p1[32]+self.data_p1[33]+self.data_p1[34])/5)
        self.prom_data_p1.append((self.data_p1[35]+self.data_p1[36]+self.data_p1[37]+self.data_p1[38]+self.data_p1[39])/5)
        self.prom_data_p1.append((self.prom_data_p1[0]+self.prom_data_p1[1]+self.prom_data_p1[2]+self.prom_data_p1[3]+self.prom_data_p1[4]+self.prom_data_p1[5]+self.prom_data_p1[6]+self.prom_data_p1[7])/8)

        self.prom_data_p2.append((self.data_p2[0]+self.data_p2[1]+self.data_p2[2]+self.data_p2[3]+self.data_p2[4])/5)
        self.prom_data_p2.append((self.data_p2[5]+self.data_p2[6]+self.data_p2[7]+self.data_p2[8]+self.data_p2[9])/5)
        self.prom_data_p2.append((self.data_p2[10]+self.data_p2[11]+self.data_p2[12]+self.data_p2[13]+self.data_p2[14])/5)
        self.prom_data_p2.append((self.data_p2[15]+self.data_p2[16]+self.data_p2[17]+self.data_p2[18]+self.data_p2[19])/5)
        self.prom_data_p2.append((self.data_p2[20]+self.data_p2[21]+self.data_p2[22]+self.data_p2[23]+self.data_p2[24])/5)
        self.prom_data_p2.append((self.data_p2[25]+self.data_p2[26]+self.data_p2[27]+self.data_p2[28]+self.data_p2[29])/5)
        self.prom_data_p2.append((self.data_p2[30]+self.data_p2[31]+self.data_p2[32]+self.data_p2[33]+self.data_p2[34])/5)
        self.prom_data_p2.append((self.data_p2[35]+self.data_p2[36]+self.data_p2[37]+self.data_p2[38]+self.data_p2[39])/5)
        self.prom_data_p2.append((self.prom_data_p2[0]+self.prom_data_p2[1]+self.prom_data_p2[2]+self.prom_data_p2[3]+self.prom_data_p2[4]+self.prom_data_p2[5]+self.prom_data_p2[6]+self.prom_data_p2[7])/8)
     
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        table_srm = self.get_table_data_srm()
        table_os = self.get_table_data_os()
        table_go = self.get_table_data_go()
        table_wam = self.get_table_data_wam()
        table_tech = self.get_table_data_tech()
        table_cust = self.get_table_data_cust()
        table_vci = self.get_table_data_vci()
        table_se = self.get_table_data_se()

        self.sum_results(table_srm, table_os, table_go, table_wam, table_tech, table_cust, table_vci, table_se)

        context['dataAct'] = [ '%.2f' % elem for elem in self.data_act ]
        context['dataP1'] = [ '%.2f' % elem for elem in self.data_p1 ]
        context['dataP2'] =  [ '%.2f' % elem for elem in self.data_p2 ]
        context['P_dataAct'] = [ '%.2f' % elem for elem in self.prom_data_act ]
        context['P_dataP1'] = [ '%.2f' % elem for elem in self.prom_data_p1 ]
        context['P_dataP2'] = [ '%.2f' % elem for elem in self.prom_data_p2 ]
        return context

###################################################################
###################################################################
class ChartsDetailView(DetailView):
    model = Questionary
    template_name_suffix = '_detail_charts'
    data_act = []
    data_p1 = []
    data_p2 = []
    prom_data_act = []
    prom_data_p1 = []
    prom_data_p2 = []
    
    def get_table_data_srm(self):
        table_data = [] #lista vacia para almacenar resultados 
        #############SMR#################
        #smr 1.1 
        if self.object.srm_11_act == 'D': 
            table_data.append(0.4*1.0)
        elif self.object.srm_11_act == 'C':
            table_data.append(0.4*0.7)
        elif self.object.srm_11_act == 'B':
            table_data.append(0.4*0.5)
        else: # A o nulo
            table_data.append(0.0)

        if self.object.srm_11_p1 == 'D': 
            table_data.append(0.4*1.0)
        elif self.object.srm_11_p1 == 'C':
            table_data.append(0.4*0.7)
        elif self.object.srm_11_p1 == 'B':
            table_data.append(0.4*0.5)
        else: # A o nulo
            table_data.append(0.0)
  
        if self.object.srm_11_p2 == 'D': 
            table_data.append(0.4*1.0)
        elif self.object.srm_11_p2 == 'C':
            table_data.append(0.4*0.7)
        elif self.object.srm_11_p2 == 'B':
            table_data.append(0.4*0.5)
        else: # A o nulo
            table_data.append(0.0)

        #smr 1.2 
        if self.object.srm_12_act == 'E': 
            table_data.append(0.35*1.0)
        elif self.object.srm_12_act == 'D': 
            table_data.append(0.35*7.0)
        elif self.object.srm_12_act == 'C':
            table_data.append(0.35*0.55)
        elif self.object.srm_12_act == 'B':
            table_data.append(0.35*0.4)
        else: # A o nulo
            table_data.append(0.0)

        if self.object.srm_12_p1 == 'E': 
            table_data.append(0.35*1.0)
        elif self.object.srm_12_p1 == 'D': 
            table_data.append(0.35*0.7)
        elif self.object.srm_12_p1 == 'C':
            table_data.append(0.35*0.55)
        elif self.object.srm_12_p1 == 'B':
            table_data.append(0.35*0.4)
        else: # A o nulo
            table_data.append(0.0)

        if self.object.srm_12_p2 == 'E': 
            table_data.append(0.35*1.0)
        elif self.object.srm_12_p2 == 'D': 
            table_data.append(0.35*7.0)
        elif self.object.srm_12_p2 == 'C':
            table_data.append(0.35*0.55)
        elif self.object.srm_12_p2 == 'B':
            table_data.append(0.35*0.4)
        else: # A o nulo
            table_data.append(0.0)

        #smr 1.3
        if self.object.srm_13_act == 'C': 
            table_data.append(0.25*1.0)
        elif self.object.srm_13_act == 'B': 
            table_data.append(0.25*7.0)
        else: # A o nulo
            table_data.append(0.0)

        if self.object.srm_13_p1 == 'C': 
            table_data.append(0.25*1.0)
        elif self.object.srm_13_p1 == 'B': 
            table_data.append(0.25*7.0)
        else: # A o nulo
            table_data.append(0.0)

        if self.object.srm_13_p2 == 'C': 
            table_data.append(0.25*1.0)
        elif self.object.srm_13_p2 == 'B': 
            table_data.append(0.25*7.0)
        else: # A o nulo
            table_data.append(0.0)

        #smr 2.1 
        if self.object.srm_21_act == 'D': 
            table_data.append(0.3*1.0)
        elif self.object.srm_21_act == 'C':
            table_data.append(0.3*0.7)
        elif self.object.srm_21_act == 'B':
            table_data.append(0.3*0.5)
        else: # A o nulo
            table_data.append(0.0)

        if self.object.srm_21_p1 == 'D': 
            table_data.append(0.3*1.0)
        elif self.object.srm_21_p1 == 'C':
            table_data.append(0.3*0.7)
        elif self.object.srm_21_p1 == 'B':
            table_data.append(0.3*0.5)
        else: # A o nulo
            table_data.append(0.0)
  
        if self.object.srm_21_p2 == 'D': 
            table_data.append(0.3*1.0)
        elif self.object.srm_21_p2 == 'C':
            table_data.append(0.3*0.7)
        elif self.object.srm_21_p2 == 'B':
            table_data.append(0.3*0.5)
        else: # A o nulo
            table_data.append(0.0)

        #smr 2.2 
        if self.object.srm_22_act == 'D': 
            table_data.append(0.15*1.0)
        elif self.object.srm_22_act == 'C':
            table_data.append(0.15*0.7)
        elif self.object.srm_22_act == 'B':
            table_data.append(0.15*0.5)
        else: # A o nulo
            table_data.append(0.0)

        if self.object.srm_22_p1 == 'D': 
            table_data.append(0.15*1.0)
        elif self.object.srm_22_p1 == 'C':
            table_data.append(0.15*0.7)
        elif self.object.srm_22_p1 == 'B':
            table_data.append(0.15*0.5)
        else: # A o nulo
            table_data.append(0.0)
  
        if self.object.srm_22_p2 == 'D': 
            table_data.append(0.15*1.0)
        elif self.object.srm_22_p2 == 'C':
            table_data.append(0.15*0.7)
        elif self.object.srm_22_p2 == 'B':
            table_data.append(0.15*0.5)
        else: # A o nulo
            table_data.append(0.0)

        #smr 2.3 
        if self.object.srm_23_act == 'D': 
            table_data.append(0.10*1.0)
        elif self.object.srm_23_act == 'C':
            table_data.append(0.10*0.7)
        elif self.object.srm_23_act == 'B':
            table_data.append(0.10*0.5)
        else: # A o nulo
            table_data.append(0.0)

        if self.object.srm_23_p1 == 'D': 
            table_data.append(0.10*1.0)
        elif self.object.srm_23_p1 == 'C':
            table_data.append(0.10*0.7)
        elif self.object.srm_23_p1 == 'B':
            table_data.append(0.10*0.5)
        else: # A o nulo
            table_data.append(0.0)
  
        if self.object.srm_23_p2 == 'D': 
            table_data.append(0.10*1.0)
        elif self.object.srm_23_p2 == 'C':
            table_data.append(0.10*0.7)
        elif self.object.srm_23_p2 == 'B':
            table_data.append(0.10*0.5)
        else: # A o nulo
            table_data.append(0.0)

        #smr 2.4
        if self.object.srm_24_act == 'D': 
            table_data.append(0.10*1.0)
        elif self.object.srm_24_act == 'C':
            table_data.append(0.10*0.55)
        elif self.object.srm_24_act == 'B':
            table_data.append(0.10*0.3)
        else: # A o nulo
            table_data.append(0.0)

        if self.object.srm_24_p1 == 'D': 
            table_data.append(0.10*1.0)
        elif self.object.srm_24_p1 == 'C':
            table_data.append(0.10*0.55)
        elif self.object.srm_24_p1 == 'B':
            table_data.append(0.10*0.3)
        else: # A o nulo
            table_data.append(0.0)
  
        if self.object.srm_24_p2 == 'D': 
            table_data.append(0.10*1.0)
        elif self.object.srm_24_p2 == 'C':
            table_data.append(0.10*0.55)
        elif self.object.srm_24_p2 == 'B':
            table_data.append(0.10*0.3)
        else: # A o nulo
            table_data.append(0.0)

        #smr 2.5 
        if self.object.srm_25_act == 'D': 
            table_data.append(0.20*1.0)
        elif self.object.srm_25_act == 'C':
            table_data.append(0.20*0.7)
        elif self.object.srm_25_act == 'B':
            table_data.append(0.20*0.5)
        else: # A o nulo
            table_data.append(0.0)

        if self.object.srm_25_p1 == 'D': 
            table_data.append(0.20*1.0)
        elif self.object.srm_25_p1 == 'C':
            table_data.append(0.20*0.7)
        elif self.object.srm_25_p1 == 'B':
            table_data.append(0.20*0.5)
        else: # A o nulo
            table_data.append(0.0)
  
        if self.object.srm_25_p2 == 'D': 
            table_data.append(0.20*1.0)
        elif self.object.srm_25_p2 == 'C':
            table_data.append(0.20*0.7)
        elif self.object.srm_25_p2 == 'B':
            table_data.append(0.20*0.5)
        else: # A o nulo
            table_data.append(0.0)
        #smr 2.6
        if self.object.srm_26_act == 'E': 
            table_data.append(0.15*1.0)
        elif self.object.srm_26_act == 'D':
            table_data.append(0.15*0.7)
        elif self.object.srm_26_act == 'C':
            table_data.append(0.15*0.5)
        elif self.object.srm_26_act == 'B':
            table_data.append(0.15*0.3)
        else: # A o nulo
            table_data.append(0.0)

        if self.object.srm_26_p1 == 'E': 
            table_data.append(0.15*1.0)
        elif self.object.srm_26_p1 == 'D':
            table_data.append(0.15*0.7)
        elif self.object.srm_26_p1 == 'C':
            table_data.append(0.15*0.5)
        elif self.object.srm_26_p1 == 'B':
            table_data.append(0.15*0.3)
        else: # A o nulo
            table_data.append(0.0)
  
        if self.object.srm_26_p2 == 'E': 
            table_data.append(0.15*1.0)
        elif self.object.srm_26_p2 == 'D':
            table_data.append(0.15*0.7)
        elif self.object.srm_26_p2 == 'C':
            table_data.append(0.15*0.5)
        elif self.object.srm_26_p2 == 'B':
            table_data.append(0.15*0.3)
        else: # A o nulo
            table_data.append(0.0)

                #smr 3.1
        if self.object.srm_31_act == 'D': 
            table_data.append(0.4*1.0)
        elif self.object.srm_31_act == 'C':
            table_data.append(0.4*0.7)
        elif self.object.srm_31_act == 'B':
            table_data.append(0.40*0.3)
        else: # A o nulo
            table_data.append(0.0)

        if self.object.srm_31_p1 == 'D': 
            table_data.append(0.4*1.0)
        elif self.object.srm_31_p1 == 'C':
            table_data.append(0.4*0.7)
        elif self.object.srm_31_p1 == 'B':
            table_data.append(0.4*0.3)
        else: # A o nulo
            table_data.append(0.0)
  
        if self.object.srm_31_p2 == 'D': 
            table_data.append(0.4*1.0)
        elif self.object.srm_31_p2 == 'C':
            table_data.append(0.4*0.7)
        elif self.object.srm_31_p2 == 'B':
            table_data.append(0.4*0.3)
        else: # A o nulo
            table_data.append(0.0)

        #smr 3.2
        if self.object.srm_32_act == 'D': 
            table_data.append(0.3*1.0)
        elif self.object.srm_32_act == 'C':
            table_data.append(0.3*0.7)
        elif self.object.srm_32_act == 'B':
            table_data.append(0.30*0.5)
        else: # A o nulo
            table_data.append(0.0)

        if self.object.srm_32_p1 == 'D': 
            table_data.append(0.3*1.0)
        elif self.object.srm_32_p1 == 'C':
            table_data.append(0.3*0.7)
        elif self.object.srm_32_p1 == 'B':
            table_data.append(0.3*0.5)
        else: # A o nulo
            table_data.append(0.0)
  
        if self.object.srm_32_p2 == 'D': 
            table_data.append(0.3*1.0)
        elif self.object.srm_32_p2 == 'C':
            table_data.append(0.3*0.7)
        elif self.object.srm_32_p2 == 'B':
            table_data.append(0.3*0.5)
        else: # A o nulo
            table_data.append(0.0)

        #smr 3.3
        if self.object.srm_33_act == 'D': 
            table_data.append(0.2*1.0)
        elif self.object.srm_33_act == 'C':
            table_data.append(0.2*0.7)
        elif self.object.srm_33_act == 'B':
            table_data.append(0.20*0.2)
        else: # A o nulo
            table_data.append(0.0)

        if self.object.srm_33_p1 == 'D': 
            table_data.append(0.2*1.0)
        elif self.object.srm_33_p1 == 'C':
            table_data.append(0.2*0.7)
        elif self.object.srm_33_p1 == 'B':
            table_data.append(0.2*0.2)
        else: # A o nulo
            table_data.append(0.0)
  
        if self.object.srm_33_p2 == 'D': 
            table_data.append(0.2*1.0)
        elif self.object.srm_33_p2 == 'C':
            table_data.append(0.2*0.7)
        elif self.object.srm_33_p2 == 'B':
            table_data.append(0.2*0.2)
        else: # A o nulo
            table_data.append(0.0)

        #smr 3.4
        if self.object.srm_34_act == 'D': 
            table_data.append(0.1*1.0)
        elif self.object.srm_34_act == 'C':
            table_data.append(0.1*0.6)
        elif self.object.srm_34_act == 'B':
            table_data.append(0.10*0.2)
        else: # A o nulo
            table_data.append(0.0)

        if self.object.srm_34_p1 == 'D': 
            table_data.append(0.1*1.0)
        elif self.object.srm_34_p1 == 'C':
            table_data.append(0.1*0.6)
        elif self.object.srm_34_p1 == 'B':
            table_data.append(0.1*0.2)
        else: # A o nulo
            table_data.append(0.0)
  
        if self.object.srm_34_p2 == 'D': 
            table_data.append(0.1*1.0)
        elif self.object.srm_34_p2 == 'C':
            table_data.append(0.1*0.6)
        elif self.object.srm_34_p2 == 'B':
            table_data.append(0.1*0.2)
        else: # A o nulo
            table_data.append(0.0)

        #smr 4.1
        if self.object.srm_41_act == 'D': 
            table_data.append(0.35*1.0)
        elif self.object.srm_41_act == 'C':
            table_data.append(0.35*0.7)
        elif self.object.srm_41_act == 'B':
            table_data.append(0.35*0.5)
        else: # A o nulo
            table_data.append(0.0)

        if self.object.srm_41_p1 == 'D': 
            table_data.append(0.35*1.0)
        elif self.object.srm_41_p1 == 'C':
            table_data.append(0.35*0.7)
        elif self.object.srm_41_p1 == 'B':
            table_data.append(0.35*0.5)
        else: # A o nulo
            table_data.append(0.0)
  
        if self.object.srm_41_p2 == 'D': 
            table_data.append(0.35*1.0)
        elif self.object.srm_41_p2 == 'C':
            table_data.append(0.35*0.7)
        elif self.object.srm_41_p2 == 'B':
            table_data.append(0.35*0.5)
        else: # A o nulo
            table_data.append(0.0)

        #smr 4.2
        if self.object.srm_42_act == 'D': 
            table_data.append(0.35*1.0)
        elif self.object.srm_42_act == 'C':
            table_data.append(0.35*0.7)
        elif self.object.srm_42_act == 'B':
            table_data.append(0.35*0.5)
        else: # A o nulo
            table_data.append(0.0)

        if self.object.srm_42_p1 == 'D': 
            table_data.append(0.35*1.0)
        elif self.object.srm_42_p1 == 'C':
            table_data.append(0.35*0.7)
        elif self.object.srm_42_p1 == 'B':
            table_data.append(0.35*0.5)
        else: # A o nulo
            table_data.append(0.0)
  
        if self.object.srm_42_p2 == 'D': 
            table_data.append(0.35*1.0)
        elif self.object.srm_42_p2 == 'C':
            table_data.append(0.35*0.7)
        elif self.object.srm_42_p2 == 'B':
            table_data.append(0.35*0.5)
        else: # A o nulo
            table_data.append(0.0)

        #smr 4.3
        if self.object.srm_43_act == 'D': 
            table_data.append(0.3*1.0)
        elif self.object.srm_43_act == 'C':
            table_data.append(0.3*0.7)
        elif self.object.srm_43_act == 'B':
            table_data.append(0.3*0.5)
        else: # A o nulo
            table_data.append(0.0)

        if self.object.srm_43_p1 == 'D': 
            table_data.append(0.3*1.0)
        elif self.object.srm_43_p1 == 'C':
            table_data.append(0.3*0.7)
        elif self.object.srm_43_p1 == 'B':
            table_data.append(0.3*0.5)
        else: # A o nulo
            table_data.append(0.0)
  
        if self.object.srm_43_p2 == 'D': 
            table_data.append(0.3*1.0)
        elif self.object.srm_43_p2 == 'C':
            table_data.append(0.3*0.7)
        elif self.object.srm_43_p2 == 'B':
            table_data.append(0.3*0.5)
        else: # A o nulo
            table_data.append(0.0)

        #smr 5.1
        if self.object.srm_51_act == 'D': 
            table_data.append(0.35*1.0)
        elif self.object.srm_51_act == 'C':
            table_data.append(0.35*0.5)
        elif self.object.srm_51_act == 'B':
            table_data.append(0.35*0.3)
        else: # A o nulo
            table_data.append(0.0)

        if self.object.srm_51_p1 == 'D': 
            table_data.append(0.35*1.0)
        elif self.object.srm_51_p1 == 'C':
            table_data.append(0.35*0.5)
        elif self.object.srm_51_p1 == 'B':
            table_data.append(0.35*0.3)
        else: # A o nulo
            table_data.append(0.0)
  
        if self.object.srm_51_p2 == 'D': 
            table_data.append(0.35*1.0)
        elif self.object.srm_51_p2 == 'C':
            table_data.append(0.35*0.5)
        elif self.object.srm_51_p2 == 'B':
            table_data.append(0.35*0.3)
        else: # A o nulo
            table_data.append(0.0)

        #smr 5.2
        if self.object.srm_52_act == 'F': 
            table_data.append(0.3*1.0)
        elif self.object.srm_52_act == 'E':
            table_data.append(0.3*0.8)
        elif self.object.srm_52_act == 'D':
            table_data.append(0.3*0.6)
        elif self.object.srm_52_act == 'C':
            table_data.append(0.3*0.4)
        elif self.object.srm_52_act == 'B':
            table_data.append(0.3*0.1)
        else: # A o nulo
            table_data.append(0.0)

        if self.object.srm_52_p1 == 'F': 
            table_data.append(0.3*1.0)
        elif self.object.srm_52_p1 == 'E':
            table_data.append(0.3*0.8)
        elif self.object.srm_52_p1 == 'D':
            table_data.append(0.3*0.6)
        elif self.object.srm_52_p1 == 'C':
            table_data.append(0.3*0.4)
        elif self.object.srm_52_p1 == 'B':
            table_data.append(0.3*0.1)
        else: # A o nulo
            table_data.append(0.0)
  
        if self.object.srm_52_p2 == 'F': 
            table_data.append(0.3*1.0)
        elif self.object.srm_52_p2 == 'E':
            table_data.append(0.3*0.8)
        elif self.object.srm_52_p2 == 'D':
            table_data.append(0.3*0.6)
        elif self.object.srm_52_p2 == 'C':
            table_data.append(0.3*0.4)
        elif self.object.srm_52_p2 == 'B':
            table_data.append(0.3*0.1)
        else: # A o nulo
            table_data.append(0.0)
        #smr 5.3
        if self.object.srm_53_act == 'D': 
            table_data.append(0.35*1.0)
        elif self.object.srm_53_act == 'C':
            table_data.append(0.35*0.5)
        elif self.object.srm_53_act == 'B':
            table_data.append(0.35*0.2)
        else: # A o nulo
            table_data.append(0.0)

        if self.object.srm_53_p1 == 'D': 
            table_data.append(0.35*1.0)
        elif self.object.srm_53_p1 == 'C':
            table_data.append(0.35*0.5)
        elif self.object.srm_53_p1 == 'B':
            table_data.append(0.35*0.2)
        else: # A o nulo
            table_data.append(0.0)
  
        if self.object.srm_53_p2 == 'D': 
            table_data.append(0.35*1.0)
        elif self.object.srm_53_p2 == 'C':
            table_data.append(0.35*0.5)
        elif self.object.srm_53_p2 == 'B':
            table_data.append(0.35*0.2)
        else: # A o nulo
            table_data.append(0.0)    
        
        return table_data

    def get_table_data_os(self):
        table_data = [] #lista vacia para almacenar resultados 
        #############OS#################
                #os 1.1
        if self.object.os_11_act == 'C': 
            table_data.append(0.33*1.0)
        elif self.object.os_11_act == 'B':
            table_data.append(0.33*0.7)
        else: # A o nulo
            table_data.append(0.0)

        if self.object.os_11_p1 == 'C': 
            table_data.append(0.33*1.0)
        elif self.object.os_11_p1 == 'B':
            table_data.append(0.33*0.7)
        else: # A o nulo
            table_data.append(0.0)
  
        if self.object.os_11_p2 == 'C': 
            table_data.append(0.33*1.0)
        elif self.object.os_11_p2 == 'B':
            table_data.append(0.33*0.7)
        else: # A o nulo
            table_data.append(0.0)

        #os 1.2
        if self.object.os_12_act == 'C': 
            table_data.append(0.33*1.0)
        elif self.object.os_12_act == 'B':
            table_data.append(0.33*0.6)
        else: # A o nulo
            table_data.append(0.0)

        if self.object.os_12_p1 == 'C': 
            table_data.append(0.33*1.0)
        elif self.object.os_12_p1 == 'B':
            table_data.append(0.33*0.6)
        else: # A o nulo
            table_data.append(0.0)
  
        if self.object.os_12_p2 == 'C': 
            table_data.append(0.33*1.0)
        elif self.object.os_12_p2 == 'B':
            table_data.append(0.33*0.6)
        else: # A o nulo
            table_data.append(0.0)

        #os 1.3
        if self.object.os_13_act == 'D': 
            table_data.append(0.34*1.0)
        elif self.object.os_13_act == 'C':
            table_data.append(0.34*0.7)
        elif self.object.os_13_act == 'B':
            table_data.append(0.34*0.5)
        else: # A o nulo
            table_data.append(0.0)

        if self.object.os_13_p1 == 'D': 
            table_data.append(0.34*1.0)
        elif self.object.os_13_p1 == 'C':
            table_data.append(0.34*0.7)
        elif self.object.os_13_p1 == 'B':
            table_data.append(0.34*0.5)
        else: # A o nulo
            table_data.append(0.0)
  
        if self.object.os_13_p2 == 'D': 
            table_data.append(0.34*1.0)
        elif self.object.os_13_p2 == 'C':
            table_data.append(0.34*0.7)
        elif self.object.os_13_p2 == 'B':
            table_data.append(0.34*0.5)
        else: # A o nulo
            table_data.append(0.0)
        #os 2.1
        if self.object.os_21_act == 'D': 
            table_data.append(0.25*1.0)
        elif self.object.os_21_act == 'C':
            table_data.append(0.25*0.7)
        elif self.object.os_21_act == 'B':
            table_data.append(0.25*0.5)
        else: # A o nulo
            table_data.append(0.0)

        if self.object.os_21_p1 == 'D': 
            table_data.append(0.25*1.0)
        elif self.object.os_21_p1 == 'C':
            table_data.append(0.25*0.7)
        elif self.object.os_21_p1 == 'B':
            table_data.append(0.25*0.5)
        else: # A o nulo
            table_data.append(0.0)
  
        if self.object.os_21_p2 == 'D': 
            table_data.append(0.25*1.0)
        elif self.object.os_21_p2 == 'C':
            table_data.append(0.25*0.7)
        elif self.object.os_21_p2 == 'B':
            table_data.append(0.25*0.5)
        else: # A o nulo
            table_data.append(0.0)

        #os 2.2
        if self.object.os_22_act == 'D': 
            table_data.append(0.22*1.0)
        elif self.object.os_22_act == 'C':
            table_data.append(0.22*0.7)
        elif self.object.os_22_act == 'B':
            table_data.append(0.22*0.5)
        else: # A o nulo
            table_data.append(0.0)

        if self.object.os_22_p1 == 'D': 
            table_data.append(0.22*1.0)
        elif self.object.os_22_p1 == 'C':
            table_data.append(0.22*0.7)
        elif self.object.os_22_p1 == 'B':
            table_data.append(0.22*0.5)
        else: # A o nulo
            table_data.append(0.0)
  
        if self.object.os_22_p2 == 'D': 
            table_data.append(0.22*1.0)
        elif self.object.os_22_p2 == 'C':
            table_data.append(0.22*0.7)
        elif self.object.os_22_p2 == 'B':
            table_data.append(0.22*0.5)
        else: # A o nulo
            table_data.append(0.0)

        #os 2.3
        if self.object.os_23_act == 'D': 
            table_data.append(0.22*1.0)
        elif self.object.os_23_act == 'C':
            table_data.append(0.22*0.7)
        elif self.object.os_23_act == 'B':
            table_data.append(0.22*0.4)
        else: # A o nulo
            table_data.append(0.0)

        if self.object.os_23_p1 == 'D': 
            table_data.append(0.22*1.0)
        elif self.object.os_23_p1 == 'C':
            table_data.append(0.22*0.7)
        elif self.object.os_23_p1 == 'B':
            table_data.append(0.22*0.4)
        else: # A o nulo
            table_data.append(0.0)
  
        if self.object.os_23_p2 == 'D': 
            table_data.append(0.22*1.0)
        elif self.object.os_23_p2 == 'C':
            table_data.append(0.22*0.7)
        elif self.object.os_23_p2 == 'B':
            table_data.append(0.22*0.4)
        else: # A o nulo
            table_data.append(0.0)

        #os 2.4
        if self.object.os_24_act == 'D': 
            table_data.append(0.15*0.8)
        elif self.object.os_24_act == 'C':
            table_data.append(0.15*0.5)
        elif self.object.os_24_act == 'B':
            table_data.append(0.15*0.3)
        else: # A o nulo
            table_data.append(0.0)

        if self.object.os_24_p1 == 'D': 
            table_data.append(0.15*0.8)
        elif self.object.os_24_p1 == 'C':
            table_data.append(0.15*0.5)
        elif self.object.os_24_p1 == 'B':
            table_data.append(0.15*0.3)
        else: # A o nulo
            table_data.append(0.0)
  
        if self.object.os_24_p2 == 'D': 
            table_data.append(0.15*0.8)
        elif self.object.os_24_p2 == 'C':
            table_data.append(0.15*0.5)
        elif self.object.os_24_p2 == 'B':
            table_data.append(0.15*0.3)
        else: # A o nulo
            table_data.append(0.0)

        #os 2.5
        if self.object.os_25_act == 'D': 
            table_data.append(0.16*1.0)
        elif self.object.os_25_act == 'C':
            table_data.append(0.16*0.7)
        elif self.object.os_25_act == 'B':
            table_data.append(0.16*0.5)
        else: # A o nulo
            table_data.append(0.0)

        if self.object.os_25_p1 == 'D': 
            table_data.append(0.16*1.0)
        elif self.object.os_25_p1 == 'C':
            table_data.append(0.16*0.7)
        elif self.object.os_25_p1 == 'B':
            table_data.append(0.16*0.5)
        else: # A o nulo
            table_data.append(0.0)
  
        if self.object.os_25_p2 == 'D': 
            table_data.append(0.15*1.0)
        elif self.object.os_25_p2 == 'C':
            table_data.append(0.15*0.7)
        elif self.object.os_25_p2 == 'B':
            table_data.append(0.15*0.5)
        else: # A o nulo
            table_data.append(0.0)

       #os 3.1
        if self.object.os_31_act == 'E': 
            table_data.append(0.25*1.0)
        elif self.object.os_31_act == 'D':
            table_data.append(0.25*0.7)
        elif self.object.os_31_act == 'C':
            table_data.append(0.25*0.5)
        elif self.object.os_31_act == 'B':
            table_data.append(0.25*0.3)
        else: # A o nulo
            table_data.append(0.0)

        if self.object.os_31_p1 == 'E': 
            table_data.append(0.25*1.0)
        elif self.object.os_31_p1 == 'D':
            table_data.append(0.25*0.7)
        elif self.object.os_31_p1 == 'C':
            table_data.append(0.25*0.5)
        elif self.object.os_31_p1 == 'B':
            table_data.append(0.25*0.3)
        else: # A o nulo
            table_data.append(0.0)
  
        if self.object.os_31_p2 == 'E': 
            table_data.append(0.25*1.0)
        elif self.object.os_31_p2 == 'D':
            table_data.append(0.25*0.7)
        elif self.object.os_31_p2 == 'C':
            table_data.append(0.25*0.5)
        elif self.object.os_31_p2 == 'B':
            table_data.append(0.25*0.3)
        else: # A o nulo
            table_data.append(0.0)
       #os 3.2
        if self.object.os_32_act == 'E': 
            table_data.append(0.2*1.0)
        elif self.object.os_32_act == 'D':
            table_data.append(0.2*0.7)
        elif self.object.os_32_act == 'C':
            table_data.append(0.2*0.5)
        elif self.object.os_32_act == 'B':
            table_data.append(0.2*0.3)
        else: # A o nulo
            table_data.append(0.0)

        if self.object.os_32_p1 == 'E': 
            table_data.append(0.2*1.0)
        elif self.object.os_32_p1 == 'D':
            table_data.append(0.2*0.7)
        elif self.object.os_32_p1 == 'C':
            table_data.append(0.2*0.5)
        elif self.object.os_32_p1 == 'B':
            table_data.append(0.2*0.3)
        else: # A o nulo
            table_data.append(0.0)
  
        if self.object.os_32_p2 == 'E': 
            table_data.append(0.2*1.0)
        elif self.object.os_32_p2 == 'D':
            table_data.append(0.2*0.7)
        elif self.object.os_32_p2 == 'C':
            table_data.append(0.2*0.5)
        elif self.object.os_32_p2 == 'B':
            table_data.append(0.2*0.3)
        else: # A o nulo
            table_data.append(0.0)
       #os 3.3
        if self.object.os_33_act == 'E': 
            table_data.append(0.1*1.0)
        elif self.object.os_33_act == 'D':
            table_data.append(0.1*0.7)
        elif self.object.os_33_act == 'C':
            table_data.append(0.1*0.5)
        elif self.object.os_33_act == 'B':
            table_data.append(0.1*0.3)
        else: # A o nulo
            table_data.append(0.0)

        if self.object.os_33_p1 == 'E': 
            table_data.append(0.1*1.0)
        elif self.object.os_33_p1 == 'D':
            table_data.append(0.1*0.7)
        elif self.object.os_33_p1 == 'C':
            table_data.append(0.1*0.5)
        elif self.object.os_33_p1 == 'B':
            table_data.append(0.1*0.3)
        else: # A o nulo
            table_data.append(0.0)
  
        if self.object.os_33_p2 == 'E': 
            table_data.append(0.1*1.0)
        elif self.object.os_33_p2 == 'D':
            table_data.append(0.1*0.7)
        elif self.object.os_33_p2 == 'C':
            table_data.append(0.1*0.5)
        elif self.object.os_33_p2 == 'B':
            table_data.append(0.1*0.3)
        else: # A o nulo
            table_data.append(0.0)
        #os 3.4
        if self.object.os_34_act == 'D': 
            table_data.append(0.2*1.0)
        elif self.object.os_34_act == 'C':
            table_data.append(0.2*0.7)
        elif self.object.os_34_act == 'B':
            table_data.append(0.2*0.5)
        else: # A o nulo
            table_data.append(0.0)

        if self.object.os_34_p1 == 'D': 
            table_data.append(0.2*1.0)
        elif self.object.os_34_p1 == 'C':
            table_data.append(0.2*0.7)
        elif self.object.os_34_p1 == 'B':
            table_data.append(0.2*0.5)
        else: # A o nulo
            table_data.append(0.0)
  
        if self.object.os_34_p2 == 'D': 
            table_data.append(0.2*1.0)
        elif self.object.os_34_p2 == 'C':
            table_data.append(0.2*0.7)
        elif self.object.os_34_p2 == 'B':
            table_data.append(0.2*0.5)
        else: # A o nulo
            table_data.append(0.0)
        
               #os 3.5
        if self.object.os_35_act == 'E': 
            table_data.append(0.1*1.0)
        elif self.object.os_35_act == 'D':
            table_data.append(0.1*0.7)
        elif self.object.os_35_act == 'C':
            table_data.append(0.1*0.3)
        elif self.object.os_35_act == 'B':
            table_data.append(0.1*0.1)
        else: # A o nulo
            table_data.append(0.0)

        if self.object.os_35_p1 == 'E': 
            table_data.append(0.1*1.0)
        elif self.object.os_35_p1 == 'D':
            table_data.append(0.1*0.7)
        elif self.object.os_35_p1 == 'C':
            table_data.append(0.1*0.3)
        elif self.object.os_35_p1 == 'B':
            table_data.append(0.1*0.1)
        else: # A o nulo
            table_data.append(0.0)
  
        if self.object.os_35_p2 == 'E': 
            table_data.append(0.1*1.0)
        elif self.object.os_35_p2 == 'D':
            table_data.append(0.1*0.7)
        elif self.object.os_35_p2 == 'C':
            table_data.append(0.1*0.3)
        elif self.object.os_35_p2 == 'B':
            table_data.append(0.1*0.1)
        else: # A o nulo
            table_data.append(0.0)
        #os 3.6
        if self.object.os_36_act == 'D': 
            table_data.append(0.15*1.0)
        elif self.object.os_36_act == 'C':
            table_data.append(0.15*0.7)
        elif self.object.os_36_act == 'B':
            table_data.append(0.15*0.5)
        else: # A o nulo
            table_data.append(0.0)

        if self.object.os_36_p1 == 'D': 
            table_data.append(0.15*1.0)
        elif self.object.os_36_p1 == 'C':
            table_data.append(0.15*0.7)
        elif self.object.os_36_p1 == 'B':
            table_data.append(0.15*0.5)
        else: # A o nulo
            table_data.append(0.0)
  
        if self.object.os_36_p2 == 'D': 
            table_data.append(0.15*1.0)
        elif self.object.os_36_p2 == 'C':
            table_data.append(0.15*0.7)
        elif self.object.os_36_p2 == 'B':
            table_data.append(0.15*0.5)
        else: # A o nulo
            table_data.append(0.0)

        #os 4.1
        if self.object.os_41_act == 'D': 
            table_data.append(0.33*1.0)
        elif self.object.os_41_act == 'C':
            table_data.append(0.33*0.7)
        elif self.object.os_41_act == 'B':
            table_data.append(0.33*0.5)
        else: # A o nulo
            table_data.append(0.0)

        if self.object.os_41_p1 == 'D': 
            table_data.append(0.33*1.0)
        elif self.object.os_41_p1 == 'C':
            table_data.append(0.33*0.7)
        elif self.object.os_41_p1 == 'B':
            table_data.append(0.33*0.5)
        else: # A o nulo
            table_data.append(0.0)
  
        if self.object.os_41_p2 == 'D': 
            table_data.append(0.33*1.0)
        elif self.object.os_41_p2 == 'C':
            table_data.append(0.33*0.7)
        elif self.object.os_41_p2 == 'B':
            table_data.append(0.33*0.5)
        else: # A o nulo
            table_data.append(0.0)

        #os 4.2
        if self.object.os_42_act == 'D': 
            table_data.append(0.33*1.0)
        elif self.object.os_42_act == 'C':
            table_data.append(0.33*0.7)
        elif self.object.os_42_act == 'B':
            table_data.append(0.33*0.5)
        else: # A o nulo
            table_data.append(0.0)

        if self.object.os_42_p1 == 'D': 
            table_data.append(0.33*1.0)
        elif self.object.os_42_p1 == 'C':
            table_data.append(0.33*0.7)
        elif self.object.os_42_p1 == 'B':
            table_data.append(0.33*0.5)
        else: # A o nulo
            table_data.append(0.0)
  
        if self.object.os_42_p2 == 'D': 
            table_data.append(0.33*1.0)
        elif self.object.os_42_p2 == 'C':
            table_data.append(0.33*0.7)
        elif self.object.os_42_p2 == 'B':
            table_data.append(0.33*0.5)
        else: # A o nulo
            table_data.append(0.0)
        #os 4.3
        if self.object.os_43_act == 'D': 
            table_data.append(0.34*1.0)
        elif self.object.os_43_act == 'C':
            table_data.append(0.34*0.7)
        elif self.object.os_43_act == 'B':
            table_data.append(0.34*0.4)
        else: # A o nulo
            table_data.append(0.0)

        if self.object.os_43_p1 == 'D': 
            table_data.append(0.34*1.0)
        elif self.object.os_43_p1 == 'C':
            table_data.append(0.34*0.7)
        elif self.object.os_43_p1 == 'B':
            table_data.append(0.34*0.4)
        else: # A o nulo
            table_data.append(0.0)
  
        if self.object.os_43_p2 == 'D': 
            table_data.append(0.34*1.0)
        elif self.object.os_43_p2 == 'C':
            table_data.append(0.34*0.7)
        elif self.object.os_43_p2 == 'B':
            table_data.append(0.34*0.4)
        else: # A o nulo
            table_data.append(0.0)
        #os 5.1
        if self.object.os_51_act == 'D': 
            table_data.append(0.4*1.0)
        elif self.object.os_51_act == 'C':
            table_data.append(0.4*0.7)
        elif self.object.os_51_act == 'B':
            table_data.append(0.4*0.5)
        else: # A o nulo
            table_data.append(0.0)

        if self.object.os_51_p1 == 'D': 
            table_data.append(0.4*1.0)
        elif self.object.os_51_p1 == 'C':
            table_data.append(0.4*0.7)
        elif self.object.os_51_p1 == 'B':
            table_data.append(0.4*0.5)
        else: # A o nulo
            table_data.append(0.0)
  
        if self.object.os_51_p2 == 'D': 
            table_data.append(0.4*1.0)
        elif self.object.os_51_p2 == 'C':
            table_data.append(0.4*0.7)
        elif self.object.os_51_p2 == 'B':
            table_data.append(0.4*0.5)
        else: # A o nulo
            table_data.append(0.0)

        #os 5.2
        if self.object.os_52_act == 'D': 
            table_data.append(0.4*1.0)
        elif self.object.os_52_act == 'C':
            table_data.append(0.4*0.7)
        elif self.object.os_52_act == 'B':
            table_data.append(0.4*0.5)
        else: # A o nulo
            table_data.append(0.0)

        if self.object.os_52_p1 == 'D': 
            table_data.append(0.4*1.0)
        elif self.object.os_52_p1 == 'C':
            table_data.append(0.4*0.7)
        elif self.object.os_52_p1 == 'B':
            table_data.append(0.4*0.5)
        else: # A o nulo
            table_data.append(0.0)
  
        if self.object.os_52_p2 == 'D': 
            table_data.append(0.4*1.0)
        elif self.object.os_52_p2 == 'C':
            table_data.append(0.4*0.7)
        elif self.object.os_52_p2 == 'B':
            table_data.append(0.4*0.5)
        else: # A o nulo
            table_data.append(0.0)

        #os 5.3
        if self.object.os_53_act == 'D': 
            table_data.append(0.2*1.0)
        elif self.object.os_53_act == 'C':
            table_data.append(0.2*0.7)
        elif self.object.os_53_act == 'B':
            table_data.append(0.2*0.5)
        else: # A o nulo
            table_data.append(0.0)

        if self.object.os_53_p1 == 'D': 
            table_data.append(0.2*1.0)
        elif self.object.os_53_p1 == 'C':
            table_data.append(0.2*0.7)
        elif self.object.os_53_p1 == 'B':
            table_data.append(0.2*0.5)
        else: # A o nulo
            table_data.append(0.0)
  
        if self.object.os_53_p2 == 'D': 
            table_data.append(0.2*1.0)
        elif self.object.os_53_p2 == 'C':
            table_data.append(0.2*0.7)
        elif self.object.os_53_p2 == 'B':
            table_data.append(0.2*0.5)
        else: # A o nulo
            table_data.append(0.0)

        return table_data

    def get_table_data_go(self):
        table_data = [] #lista vacia para almacenar resultados 
        #############GO#################
        #go 1.1
        if self.object.go_11_act == 'D': 
            table_data.append(0.2*1.0)
        elif self.object.go_11_act == 'C':
            table_data.append(0.2*0.7)
        elif self.object.go_11_act == 'B':
            table_data.append(0.2*0.5)
        else: # A o nulo
            table_data.append(0.0)

        if self.object.go_11_p1 == 'D': 
            table_data.append(0.2*1.0)
        elif self.object.go_11_p1 == 'C':
            table_data.append(0.2*0.7)
        elif self.object.go_11_p1 == 'B':
            table_data.append(0.2*0.5)
        else: # A o nulo
            table_data.append(0.0)
  
        if self.object.go_11_p2 == 'D': 
            table_data.append(0.2*1.0)
        elif self.object.go_11_p2 == 'C':
            table_data.append(0.2*0.7)
        elif self.object.go_11_p2 == 'B':
            table_data.append(0.2*0.5)
        else: # A o nulo
            table_data.append(0.0)
        #go 1.2
        if self.object.go_12_act == 'D': 
            table_data.append(0.2*1.0)
        elif self.object.go_12_act == 'C':
            table_data.append(0.2*0.7)
        elif self.object.go_12_act == 'B':
            table_data.append(0.2*0.3)
        else: # A o nulo
            table_data.append(0.0)

        if self.object.go_12_p1 == 'D': 
            table_data.append(0.2*1.0)
        elif self.object.go_12_p1 == 'C':
            table_data.append(0.2*0.7)
        elif self.object.go_12_p1 == 'B':
            table_data.append(0.2*0.3)
        else: # A o nulo
            table_data.append(0.0)
  
        if self.object.go_12_p2 == 'D': 
            table_data.append(0.2*1.0)
        elif self.object.go_12_p2 == 'C':
            table_data.append(0.2*0.7)
        elif self.object.go_12_p2 == 'B':
            table_data.append(0.2*0.3)
        else: # A o nulo
            table_data.append(0.0)
        #go 1.3
        if self.object.go_13_act == 'D': 
            table_data.append(0.2*1.0)
        elif self.object.go_13_act == 'C':
            table_data.append(0.2*0.7)
        elif self.object.go_13_act == 'B':
            table_data.append(0.2*0.3)
        else: # A o nulo
            table_data.append(0.0)

        if self.object.go_13_p1 == 'D': 
            table_data.append(0.2*1.0)
        elif self.object.go_13_p1 == 'C':
            table_data.append(0.2*0.7)
        elif self.object.go_13_p1 == 'B':
            table_data.append(0.2*0.3)
        else: # A o nulo
            table_data.append(0.0)
  
        if self.object.go_13_p2 == 'D': 
            table_data.append(0.2*1.0)
        elif self.object.go_13_p2 == 'C':
            table_data.append(0.2*0.7)
        elif self.object.go_13_p2 == 'B':
            table_data.append(0.2*0.3)
        else: # A o nulo
            table_data.append(0.0)
        #go 1.4
        if self.object.go_14_act == 'D': 
            table_data.append(0.2*1.0)
        elif self.object.go_14_act == 'C':
            table_data.append(0.2*0.7)
        elif self.object.go_14_act == 'B':
            table_data.append(0.2*0.3)
        else: # A o nulo
            table_data.append(0.0)

        if self.object.go_14_p1 == 'D': 
            table_data.append(0.2*1.0)
        elif self.object.go_14_p1 == 'C':
            table_data.append(0.2*0.7)
        elif self.object.go_14_p1 == 'B':
            table_data.append(0.2*0.3)
        else: # A o nulo
            table_data.append(0.0)
  
        if self.object.go_14_p2 == 'D': 
            table_data.append(0.2*1.0)
        elif self.object.go_14_p2 == 'C':
            table_data.append(0.2*0.7)
        elif self.object.go_14_p2 == 'B':
            table_data.append(0.2*0.3)
        else: # A o nulo
            table_data.append(0.0)
        #go 1.5
        if self.object.go_15_act == 'D': 
            table_data.append(0.2*1.0)
        elif self.object.go_15_act == 'C':
            table_data.append(0.2*0.7)
        elif self.object.go_15_act == 'B':
            table_data.append(0.2*0.4)
        else: # A o nulo
            table_data.append(0.0)

        if self.object.go_15_p1 == 'D': 
            table_data.append(0.2*1.0)
        elif self.object.go_15_p1 == 'C':
            table_data.append(0.2*0.7)
        elif self.object.go_15_p1 == 'B':
            table_data.append(0.2*0.4)
        else: # A o nulo
            table_data.append(0.0)
  
        if self.object.go_15_p2 == 'D': 
            table_data.append(0.2*1.0)
        elif self.object.go_15_p2 == 'C':
            table_data.append(0.2*0.7)
        elif self.object.go_15_p2 == 'B':
            table_data.append(0.2*0.4)
        else: # A o nulo
            table_data.append(0.0)
       #go 2.1
        if self.object.go_21_act == 'E': 
            table_data.append(0.27*1.0)
        elif self.object.go_21_act == 'D':
            table_data.append(0.27*0.7)
        elif self.object.go_21_act == 'C':
            table_data.append(0.27*0.5)
        elif self.object.go_21_act == 'B':
            table_data.append(0.27*0.3)
        else: # A o nulo
            table_data.append(0.0)

        if self.object.go_21_p1 == 'E': 
            table_data.append(0.27*1.0)
        elif self.object.go_21_p1 == 'D':
            table_data.append(0.27*0.7)
        elif self.object.go_21_p1 == 'C':
            table_data.append(0.27*0.5)
        elif self.object.go_21_p1 == 'B':
            table_data.append(0.27*0.3)
        else: # A o nulo
            table_data.append(0.0)
  
        if self.object.go_21_p2 == 'E': 
            table_data.append(0.27*1.0)
        elif self.object.go_21_p2 == 'D':
            table_data.append(0.27*0.7)
        elif self.object.go_21_p2 == 'C':
            table_data.append(0.27*0.5)
        elif self.object.go_21_p2 == 'B':
            table_data.append(0.27*0.3)
        else: # A o nulo
            table_data.append(0.0)
        #go 2.2
        if self.object.go_22_act == 'D': 
            table_data.append(0.2*1.0)
        elif self.object.go_22_act == 'C':
            table_data.append(0.2*0.7)
        elif self.object.go_22_act == 'B':
            table_data.append(0.2*0.3)
        else: # A o nulo
            table_data.append(0.0)

        if self.object.go_22_p1 == 'D': 
            table_data.append(0.2*1.0)
        elif self.object.go_22_p1 == 'C':
            table_data.append(0.2*0.7)
        elif self.object.go_22_p1 == 'B':
            table_data.append(0.2*0.3)
        else: # A o nulo
            table_data.append(0.0)
  
        if self.object.go_22_p2 == 'D': 
            table_data.append(0.2*1.0)
        elif self.object.go_22_p2 == 'C':
            table_data.append(0.2*0.7)
        elif self.object.go_22_p2 == 'B':
            table_data.append(0.2*0.3)
        else: # A o nulo
            table_data.append(0.0)
        #go 2.3
        if self.object.go_23_act == 'D': 
            table_data.append(0.26*1.0)
        elif self.object.go_23_act == 'C':
            table_data.append(0.26*0.7)
        elif self.object.go_23_act == 'B':
            table_data.append(0.26*0.3)
        else: # A o nulo
            table_data.append(0.0)

        if self.object.go_23_p1 == 'D': 
            table_data.append(0.26*1.0)
        elif self.object.go_23_p1 == 'C':
            table_data.append(0.26*0.7)
        elif self.object.go_23_p1 == 'B':
            table_data.append(0.26*0.3)
        else: # A o nulo
            table_data.append(0.0)
  
        if self.object.go_23_p2 == 'D': 
            table_data.append(0.26*1.0)
        elif self.object.go_23_p2 == 'C':
            table_data.append(0.26*0.7)
        elif self.object.go_23_p2 == 'B':
            table_data.append(0.26*0.3)
        else: # A o nulo
            table_data.append(0.0)
       #go 2.4
        if self.object.go_24_act == 'E': 
            table_data.append(0.27*1.0)
        elif self.object.go_24_act == 'D':
            table_data.append(0.27*0.7)
        elif self.object.go_24_act == 'C':
            table_data.append(0.27*0.5)
        elif self.object.go_24_act == 'B':
            table_data.append(0.27*0.3)
        else: # A o nulo
            table_data.append(0.0)

        if self.object.go_24_p1 == 'E': 
            table_data.append(0.27*1.0)
        elif self.object.go_24_p1 == 'D':
            table_data.append(0.27*0.7)
        elif self.object.go_24_p1 == 'C':
            table_data.append(0.27*0.5)
        elif self.object.go_24_p1 == 'B':
            table_data.append(0.27*0.3)
        else: # A o nulo
            table_data.append(0.0)
  
        if self.object.go_24_p2 == 'E': 
            table_data.append(0.27*1.0)
        elif self.object.go_24_p2 == 'D':
            table_data.append(0.27*0.7)
        elif self.object.go_24_p2 == 'C':
            table_data.append(0.27*0.5)
        elif self.object.go_24_p2 == 'B':
            table_data.append(0.27*0.3)
        else: # A o nulo
            table_data.append(0.0)
        #go 3.1
        if self.object.go_31_act == 'D': 
            table_data.append(0.18*1.0)
        elif self.object.go_31_act == 'C':
            table_data.append(0.18*0.5)
        elif self.object.go_31_act == 'B':
            table_data.append(0.18*0.3)
        else: # A o nulo
            table_data.append(0.0)

        if self.object.go_31_p1 == 'D': 
            table_data.append(0.18*1.0)
        elif self.object.go_31_p1 == 'C':
            table_data.append(0.18*0.5)
        elif self.object.go_31_p1 == 'B':
            table_data.append(0.18*0.3)
        else: # A o nulo
            table_data.append(0.0)
  
        if self.object.go_31_p2 == 'D': 
            table_data.append(0.18*1.0)
        elif self.object.go_31_p2 == 'C':
            table_data.append(0.18*0.5)
        elif self.object.go_31_p2 == 'B':
            table_data.append(0.18*0.3)
        else: # A o nulo
            table_data.append(0.0)
        #go 3.2
        if self.object.go_32_act == 'D': 
            table_data.append(0.1*1.0)
        elif self.object.go_32_act == 'C':
            table_data.append(0.1*0.7)
        elif self.object.go_32_act == 'B':
            table_data.append(0.1*0.5)
        else: # A o nulo
            table_data.append(0.0)

        if self.object.go_32_p1 == 'D': 
            table_data.append(0.1*1.0)
        elif self.object.go_32_p1 == 'C':
            table_data.append(0.1*0.7)
        elif self.object.go_32_p1 == 'B':
            table_data.append(0.1*0.5)
        else: # A o nulo
            table_data.append(0.0)
  
        if self.object.go_32_p2 == 'D': 
            table_data.append(0.1*1.0)
        elif self.object.go_32_p2 == 'C':
            table_data.append(0.1*0.7)
        elif self.object.go_32_p2 == 'B':
            table_data.append(0.1*0.5)
        else: # A o nulo
            table_data.append(0.0)
       #go 3.3
        if self.object.go_33_act == 'E': 
            table_data.append(0.18*1.0)
        elif self.object.go_33_act == 'D':
            table_data.append(0.18*0.7)
        elif self.object.go_33_act == 'C':
            table_data.append(0.18*0.5)
        elif self.object.go_33_act == 'B':
            table_data.append(0.18*0.2)
        else: # A o nulo
            table_data.append(0.0)

        if self.object.go_33_p1 == 'E': 
            table_data.append(0.18*1.0)
        elif self.object.go_33_p1 == 'D':
            table_data.append(0.18*0.7)
        elif self.object.go_33_p1 == 'C':
            table_data.append(0.18*0.5)
        elif self.object.go_33_p1 == 'B':
            table_data.append(0.18*0.2)
        else: # A o nulo
            table_data.append(0.0)
  
        if self.object.go_33_p2 == 'E': 
            table_data.append(0.18*1.0)
        elif self.object.go_33_p2 == 'D':
            table_data.append(0.18*0.7)
        elif self.object.go_33_p2 == 'C':
            table_data.append(0.18*0.5)
        elif self.object.go_33_p2 == 'B':
            table_data.append(0.18*0.2)
        else: # A o nulo
            table_data.append(0.0)
        #go 3.4
        if self.object.go_34_act == 'D': 
            table_data.append(0.18*1.0)
        elif self.object.go_34_act == 'C':
            table_data.append(0.18*0.5)
        elif self.object.go_34_act == 'B':
            table_data.append(0.18*0.3)
        else: # A o nulo
            table_data.append(0.0)

        if self.object.go_34_p1 == 'D': 
            table_data.append(0.18*1.0)
        elif self.object.go_34_p1 == 'C':
            table_data.append(0.18*0.5)
        elif self.object.go_34_p1 == 'B':
            table_data.append(0.18*0.3)
        else: # A o nulo
            table_data.append(0.0)
  
        if self.object.go_34_p2 == 'D': 
            table_data.append(0.18*1.0)
        elif self.object.go_34_p2 == 'C':
            table_data.append(0.18*0.5)
        elif self.object.go_34_p2 == 'B':
            table_data.append(0.18*0.3)
        else: # A o nulo
            table_data.append(0.0)
       #go 3.5
        if self.object.go_35_act == 'E': 
            table_data.append(0.18*1.0)
        elif self.object.go_35_act == 'D':
            table_data.append(0.18*0.7)
        elif self.object.go_35_act == 'C':
            table_data.append(0.18*0.5)
        elif self.object.go_35_act == 'B':
            table_data.append(0.18*0.3)
        else: # A o nulo
            table_data.append(0.0)

        if self.object.go_35_p1 == 'E': 
            table_data.append(0.18*1.0)
        elif self.object.go_35_p1 == 'D':
            table_data.append(0.18*0.7)
        elif self.object.go_35_p1 == 'C':
            table_data.append(0.18*0.5)
        elif self.object.go_35_p1 == 'B':
            table_data.append(0.18*0.3)
        else: # A o nulo
            table_data.append(0.0)
  
        if self.object.go_35_p2 == 'E': 
            table_data.append(0.18*1.0)
        elif self.object.go_35_p2 == 'D':
            table_data.append(0.18*0.7)
        elif self.object.go_35_p2 == 'C':
            table_data.append(0.18*0.5)
        elif self.object.go_35_p2 == 'B':
            table_data.append(0.18*0.3)
        else: # A o nulo
            table_data.append(0.0)
       #go 3.6
        if self.object.go_36_act == 'E': 
            table_data.append(0.18*1.0)
        elif self.object.go_36_act == 'D':
            table_data.append(0.18*0.7)
        elif self.object.go_36_act == 'C':
            table_data.append(0.18*0.5)
        elif self.object.go_36_act == 'B':
            table_data.append(0.18*0.3)
        else: # A o nulo
            table_data.append(0.0)

        if self.object.go_36_p1 == 'E': 
            table_data.append(0.18*1.0)
        elif self.object.go_36_p1 == 'D':
            table_data.append(0.18*0.7)
        elif self.object.go_36_p1 == 'C':
            table_data.append(0.18*0.5)
        elif self.object.go_36_p1 == 'B':
            table_data.append(0.18*0.3)
        else: # A o nulo
            table_data.append(0.0)
  
        if self.object.go_36_p2 == 'E': 
            table_data.append(0.18*1.0)
        elif self.object.go_36_p2 == 'D':
            table_data.append(0.18*0.7)
        elif self.object.go_36_p2 == 'C':
            table_data.append(0.18*0.5)
        elif self.object.go_36_p2 == 'B':
            table_data.append(0.18*0.3)
        else: # A o nulo
            table_data.append(0.0)
        #go 4.1
        if self.object.go_41_act == 'D': 
            table_data.append(0.2*1.0)
        elif self.object.go_41_act == 'C':
            table_data.append(0.2*0.7)
        elif self.object.go_41_act == 'B':
            table_data.append(0.2*0.4)
        else: # A o nulo
            table_data.append(0.0)

        if self.object.go_41_p1 == 'D': 
            table_data.append(0.2*1.0)
        elif self.object.go_41_p1 == 'C':
            table_data.append(0.2*0.7)
        elif self.object.go_41_p1 == 'B':
            table_data.append(0.2*0.4)
        else: # A o nulo
            table_data.append(0.0)
  
        if self.object.go_41_p2 == 'D': 
            table_data.append(0.2*1.0)
        elif self.object.go_41_p2 == 'C':
            table_data.append(0.2*0.7)
        elif self.object.go_41_p2 == 'B':
            table_data.append(0.2*0.4)
        else: # A o nulo
            table_data.append(0.0)
       #go 4.2
        if self.object.go_42_act == 'E': 
            table_data.append(0.2*1.0)
        elif self.object.go_42_act == 'D':
            table_data.append(0.2*0.8)
        elif self.object.go_42_act == 'C':
            table_data.append(0.2*0.5)
        elif self.object.go_42_act == 'B':
            table_data.append(0.2*0.2)
        else: # A o nulo
            table_data.append(0.0)

        if self.object.go_42_p1 == 'E': 
            table_data.append(0.2*1.0)
        elif self.object.go_42_p1 == 'D':
            table_data.append(0.2*0.8)
        elif self.object.go_42_p1 == 'C':
            table_data.append(0.2*0.5)
        elif self.object.go_42_p1 == 'B':
            table_data.append(0.2*0.2)
        else: # A o nulo
            table_data.append(0.0)
  
        if self.object.go_42_p2 == 'E': 
            table_data.append(0.2*1.0)
        elif self.object.go_42_p2 == 'D':
            table_data.append(0.2*0.8)
        elif self.object.go_42_p2 == 'C':
            table_data.append(0.2*0.5)
        elif self.object.go_42_p2 == 'B':
            table_data.append(0.2*0.2)
        else: # A o nulo
            table_data.append(0.0)
       #go 4.3
        if self.object.go_43_act == 'E': 
            table_data.append(0.2*1.0)
        elif self.object.go_43_act == 'D':
            table_data.append(0.2*0.8)
        elif self.object.go_43_act == 'C':
            table_data.append(0.2*0.5)
        elif self.object.go_43_act == 'B':
            table_data.append(0.2*0.2)
        else: # A o nulo
            table_data.append(0.0)

        if self.object.go_43_p1 == 'E': 
            table_data.append(0.2*1.0)
        elif self.object.go_43_p1 == 'D':
            table_data.append(0.2*0.8)
        elif self.object.go_43_p1 == 'C':
            table_data.append(0.2*0.5)
        elif self.object.go_43_p1 == 'B':
            table_data.append(0.2*0.2)
        else: # A o nulo
            table_data.append(0.0)
  
        if self.object.go_43_p2 == 'E': 
            table_data.append(0.2*1.0)
        elif self.object.go_43_p2 == 'D':
            table_data.append(0.2*0.8)
        elif self.object.go_43_p2 == 'C':
            table_data.append(0.2*0.5)
        elif self.object.go_43_p2 == 'B':
            table_data.append(0.2*0.2)
        else: # A o nulo
            table_data.append(0.0)
        #go 4.4
        if self.object.go_44_act == 'D': 
            table_data.append(0.2*1.0)
        elif self.object.go_44_act == 'C':
            table_data.append(0.2*0.7)
        elif self.object.go_44_act == 'B':
            table_data.append(0.2*0.3)
        else: # A o nulo
            table_data.append(0.0)

        if self.object.go_44_p1 == 'D': 
            table_data.append(0.2*1.0)
        elif self.object.go_44_p1 == 'C':
            table_data.append(0.2*0.7)
        elif self.object.go_44_p1 == 'B':
            table_data.append(0.2*0.3)
        else: # A o nulo
            table_data.append(0.0)
  
        if self.object.go_44_p2 == 'D': 
            table_data.append(0.2*1.0)
        elif self.object.go_44_p2 == 'C':
            table_data.append(0.2*0.7)
        elif self.object.go_44_p2 == 'B':
            table_data.append(0.2*0.3)
        else: # A o nulo
            table_data.append(0.0)
        #go 4.5
        if self.object.go_45_act == 'D': 
            table_data.append(0.2*1.0)
        elif self.object.go_45_act == 'C':
            table_data.append(0.2*0.5)
        elif self.object.go_45_act == 'B':
            table_data.append(0.2*0.3)
        else: # A o nulo
            table_data.append(0.0)

        if self.object.go_45_p1 == 'D': 
            table_data.append(0.2*1.0)
        elif self.object.go_45_p1 == 'C':
            table_data.append(0.2*0.5)
        elif self.object.go_45_p1 == 'B':
            table_data.append(0.2*0.3)
        else: # A o nulo
            table_data.append(0.0)
  
        if self.object.go_45_p2 == 'D': 
            table_data.append(0.2*1.0)
        elif self.object.go_45_p2 == 'C':
            table_data.append(0.2*0.5)
        elif self.object.go_45_p2 == 'B':
            table_data.append(0.2*0.3)
        else: # A o nulo
            table_data.append(0.0)
       #go 5.1
        if self.object.go_51_act == 'E': 
            table_data.append(0.4*1.0)
        elif self.object.go_51_act == 'D':
            table_data.append(0.4*0.7)
        elif self.object.go_51_act == 'C':
            table_data.append(0.4*0.3)
        elif self.object.go_51_act == 'B':
            table_data.append(0.4*0.15)
        else: # A o nulo
            table_data.append(0.0)

        if self.object.go_51_p1 == 'E': 
            table_data.append(0.4*1.0)
        elif self.object.go_51_p1 == 'D':
            table_data.append(0.4*0.7)
        elif self.object.go_51_p1 == 'C':
            table_data.append(0.4*0.3)
        elif self.object.go_51_p1 == 'B':
            table_data.append(0.4*0.15)
        else: # A o nulo
            table_data.append(0.0)
  
        if self.object.go_51_p2 == 'E': 
            table_data.append(0.4*1.0)
        elif self.object.go_51_p2 == 'D':
            table_data.append(0.4*0.7)
        elif self.object.go_51_p2 == 'C':
            table_data.append(0.4*0.3)
        elif self.object.go_51_p2 == 'B':
            table_data.append(0.4*0.15)
        else: # A o nulo
            table_data.append(0.0)
        #go 5.2
        if self.object.go_52_act == 'D': 
            table_data.append(0.6*1.0)
        elif self.object.go_52_act == 'C':
            table_data.append(0.6*0.7)
        elif self.object.go_52_act == 'B':
            table_data.append(0.6*0.3)
        else: # A o nulo
            table_data.append(0.0)

        if self.object.go_52_p1 == 'D': 
            table_data.append(0.6*1.0)
        elif self.object.go_52_p1 == 'C':
            table_data.append(0.6*0.7)
        elif self.object.go_52_p1 == 'B':
            table_data.append(0.6*0.3)
        else: # A o nulo
            table_data.append(0.0)
  
        if self.object.go_52_p2 == 'D': 
            table_data.append(0.6*1.0)
        elif self.object.go_52_p2 == 'C':
            table_data.append(0.6*0.7)
        elif self.object.go_52_p2 == 'B':
            table_data.append(0.6*0.3)
        else: # A o nulo
            table_data.append(0.0)

        return table_data

    def get_table_data_wam(self):
        table_data = [] #lista vacia para almacenar resultados 
        #############WAM#################
                #wam 1.1
        if self.object.wam_11_act == 'D': 
            table_data.append(0.35*1.0)
        elif self.object.wam_11_act == 'C':
            table_data.append(0.35*0.7)
        elif self.object.wam_11_act == 'B':
            table_data.append(0.35*0.5)
        else: # A o nulo
            table_data.append(0.0)

        if self.object.wam_11_p1 == 'D': 
            table_data.append(0.35*1.0)
        elif self.object.wam_11_p1 == 'C':
            table_data.append(0.35*0.7)
        elif self.object.wam_11_p1 == 'B':
            table_data.append(0.35*0.5)
        else: # A o nulo
            table_data.append(0.0)
  
        if self.object.wam_11_p2 == 'D': 
            table_data.append(0.35*1.0)
        elif self.object.wam_11_p2 == 'C':
            table_data.append(0.35*0.7)
        elif self.object.wam_11_p2 == 'B':
            table_data.append(0.35*0.5)
        else: # A o nulo
            table_data.append(0.0)
        #wam 1.2
        if self.object.wam_12_act == 'D': 
            table_data.append(0.3*1.0)
        elif self.object.wam_12_act == 'C':
            table_data.append(0.3*0.7)
        elif self.object.wam_12_act == 'B':
            table_data.append(0.3*0.3)
        else: # A o nulo
            table_data.append(0.0)

        if self.object.wam_12_p1 == 'D': 
            table_data.append(0.3*1.0)
        elif self.object.wam_12_p1 == 'C':
            table_data.append(0.3*0.7)
        elif self.object.wam_12_p1 == 'B':
            table_data.append(0.3*0.3)
        else: # A o nulo
            table_data.append(0.0)
  
        if self.object.wam_12_p2 == 'D': 
            table_data.append(0.3*1.0)
        elif self.object.wam_12_p2 == 'C':
            table_data.append(0.3*0.7)
        elif self.object.wam_12_p2 == 'B':
            table_data.append(0.3*0.3)
        else: # A o nulo
            table_data.append(0.0)
        #wam 1.3
        if self.object.wam_13_act == 'D': 
            table_data.append(0.35*1.0)
        elif self.object.wam_13_act == 'C':
            table_data.append(0.35*0.7)
        elif self.object.wam_13_act == 'B':
            table_data.append(0.35*0.2)
        else: # A o nulo
            table_data.append(0.0)

        if self.object.wam_13_p1 == 'D': 
            table_data.append(0.35*1.0)
        elif self.object.wam_13_p1 == 'C':
            table_data.append(0.35*0.7)
        elif self.object.wam_13_p1 == 'B':
            table_data.append(0.35*0.2)
        else: # A o nulo
            table_data.append(0.0)
  
        if self.object.wam_13_p2 == 'D': 
            table_data.append(0.35*1.0)
        elif self.object.wam_13_p2 == 'C':
            table_data.append(0.35*0.7)
        elif self.object.wam_13_p2 == 'B':
            table_data.append(0.35*0.2)
        else: # A o nulo
            table_data.append(0.0)
       #wam 2.1
        if self.object.wam_21_act == 'E': 
            table_data.append(0.45*1.0)
        elif self.object.wam_21_act == 'D':
            table_data.append(0.45*0.7)
        elif self.object.wam_21_act == 'C':
            table_data.append(0.45*0.5)
        elif self.object.wam_21_act == 'B':
            table_data.append(0.45*0.3)
        else: # A o nulo
            table_data.append(0.0)

        if self.object.wam_21_p1 == 'E': 
            table_data.append(0.45*1.0)
        elif self.object.wam_21_p1 == 'D':
            table_data.append(0.45*0.7)
        elif self.object.wam_21_p1 == 'C':
            table_data.append(0.45*0.5)
        elif self.object.wam_21_p1 == 'B':
            table_data.append(0.45*0.3)
        else: # A o nulo
            table_data.append(0.0)
  
        if self.object.wam_21_p2 == 'E': 
            table_data.append(0.45*1.0)
        elif self.object.wam_21_p2 == 'D':
            table_data.append(0.45*0.7)
        elif self.object.wam_21_p2 == 'C':
            table_data.append(0.45*0.5)
        elif self.object.wam_21_p2 == 'B':
            table_data.append(0.45*0.3)
        else: # A o nulo
            table_data.append(0.0)
       #wam 2.2
        if self.object.wam_22_act == 'E': 
            table_data.append(0.35*1.0)
        elif self.object.wam_22_act == 'D':
            table_data.append(0.35*0.7)
        elif self.object.wam_22_act == 'C':
            table_data.append(0.35*0.5)
        elif self.object.wam_22_act == 'B':
            table_data.append(0.35*0.3)
        else: # A o nulo
            table_data.append(0.0)

        if self.object.wam_22_p1 == 'E': 
            table_data.append(0.35*1.0)
        elif self.object.wam_22_p1 == 'D':
            table_data.append(0.35*0.7)
        elif self.object.wam_22_p1 == 'C':
            table_data.append(0.35*0.5)
        elif self.object.wam_22_p1 == 'B':
            table_data.append(0.35*0.3)
        else: # A o nulo
            table_data.append(0.0)
  
        if self.object.wam_22_p2 == 'E': 
            table_data.append(0.35*1.0)
        elif self.object.wam_22_p2 == 'D':
            table_data.append(0.35*0.7)
        elif self.object.wam_22_p2 == 'C':
            table_data.append(0.35*0.5)
        elif self.object.wam_22_p2 == 'B':
            table_data.append(0.35*0.3)
        else: # A o nulo
            table_data.append(0.0)
        #wam 2.3
        if self.object.wam_23_act == 'D': 
            table_data.append(0.2*1.0)
        elif self.object.wam_23_act == 'C':
            table_data.append(0.2*0.5)
        elif self.object.wam_23_act == 'B':
            table_data.append(0.2*0.3)
        else: # A o nulo
            table_data.append(0.0)

        if self.object.wam_23_p1 == 'D': 
            table_data.append(0.2*1.0)
        elif self.object.wam_23_p1 == 'C':
            table_data.append(0.2*0.5)
        elif self.object.wam_23_p1 == 'B':
            table_data.append(0.2*0.3)
        else: # A o nulo
            table_data.append(0.0)
  
        if self.object.wam_23_p2 == 'D': 
            table_data.append(0.2*1.0)
        elif self.object.wam_23_p2 == 'C':
            table_data.append(0.2*0.5)
        elif self.object.wam_23_p2 == 'B':
            table_data.append(0.2*0.3)
        else: # A o nulo
            table_data.append(0.0)
       #wam 3.1
        if self.object.wam_31_act == 'E': 
            table_data.append(0.14*1.0)
        elif self.object.wam_31_act == 'D':
            table_data.append(0.14*0.7)
        elif self.object.wam_31_act == 'C':
            table_data.append(0.14*0.4)
        elif self.object.wam_31_act == 'B':
            table_data.append(0.14*0.2)
        else: # A o nulo
            table_data.append(0.0)

        if self.object.wam_31_p1 == 'E': 
            table_data.append(0.14*1.0)
        elif self.object.wam_31_p1 == 'D':
            table_data.append(0.14*0.7)
        elif self.object.wam_31_p1 == 'C':
            table_data.append(0.14*0.4)
        elif self.object.wam_31_p1 == 'B':
            table_data.append(0.14*0.2)
        else: # A o nulo
            table_data.append(0.0)
  
        if self.object.wam_31_p2 == 'E': 
            table_data.append(0.14*1.0)
        elif self.object.wam_31_p2 == 'D':
            table_data.append(0.14*0.7)
        elif self.object.wam_31_p2 == 'C':
            table_data.append(0.14*0.4)
        elif self.object.wam_31_p2 == 'B':
            table_data.append(0.14*0.2)
        else: # A o nulo
            table_data.append(0.0)
       #wam 3.2
        if self.object.wam_32_act == 'E': 
            table_data.append(0.14*1.0)
        elif self.object.wam_32_act == 'D':
            table_data.append(0.14*0.7)
        elif self.object.wam_32_act == 'C':
            table_data.append(0.14*0.4)
        elif self.object.wam_32_act == 'B':
            table_data.append(0.14*0.2)
        else: # A o nulo
            table_data.append(0.0)

        if self.object.wam_32_p1 == 'E': 
            table_data.append(0.14*1.0)
        elif self.object.wam_32_p1 == 'D':
            table_data.append(0.14*0.7)
        elif self.object.wam_32_p1 == 'C':
            table_data.append(0.14*0.4)
        elif self.object.wam_32_p1 == 'B':
            table_data.append(0.14*0.2)
        else: # A o nulo
            table_data.append(0.0)
  
        if self.object.wam_32_p2 == 'E': 
            table_data.append(0.14*1.0)
        elif self.object.wam_32_p2 == 'D':
            table_data.append(0.14*0.7)
        elif self.object.wam_32_p2 == 'C':
            table_data.append(0.14*0.4)
        elif self.object.wam_32_p2 == 'B':
            table_data.append(0.14*0.2)
        else: # A o nulo
            table_data.append(0.0)
       #wam 3.3
        if self.object.wam_33_act == 'E': 
            table_data.append(0.14*1.0)
        elif self.object.wam_33_act == 'D':
            table_data.append(0.14*0.7)
        elif self.object.wam_33_act == 'C':
            table_data.append(0.14*0.5)
        elif self.object.wam_33_act == 'B':
            table_data.append(0.14*0.3)
        else: # A o nulo
            table_data.append(0.0)

        if self.object.wam_33_p1 == 'E': 
            table_data.append(0.14*1.0)
        elif self.object.wam_33_p1 == 'D':
            table_data.append(0.14*0.7)
        elif self.object.wam_33_p1 == 'C':
            table_data.append(0.14*0.5)
        elif self.object.wam_33_p1 == 'B':
            table_data.append(0.14*0.3)
        else: # A o nulo
            table_data.append(0.0)
  
        if self.object.wam_33_p2 == 'E': 
            table_data.append(0.14*1.0)
        elif self.object.wam_33_p2 == 'D':
            table_data.append(0.14*0.7)
        elif self.object.wam_33_p2 == 'C':
            table_data.append(0.14*0.5)
        elif self.object.wam_33_p2 == 'B':
            table_data.append(0.14*0.3)
        else: # A o nulo
            table_data.append(0.0)
       #wam 3.4
        if self.object.wam_34_act == 'E': 
            table_data.append(0.14*1.0)
        elif self.object.wam_34_act == 'D':
            table_data.append(0.14*0.7)
        elif self.object.wam_34_act == 'C':
            table_data.append(0.14*0.5)
        elif self.object.wam_34_act == 'B':
            table_data.append(0.14*0.3)
        else: # A o nulo
            table_data.append(0.0)

        if self.object.wam_34_p1 == 'E': 
            table_data.append(0.14*1.0)
        elif self.object.wam_34_p1 == 'D':
            table_data.append(0.14*0.7)
        elif self.object.wam_34_p1 == 'C':
            table_data.append(0.14*0.5)
        elif self.object.wam_34_p1 == 'B':
            table_data.append(0.14*0.3)
        else: # A o nulo
            table_data.append(0.0)
  
        if self.object.wam_34_p2 == 'E': 
            table_data.append(0.14*1.0)
        elif self.object.wam_34_p2 == 'D':
            table_data.append(0.14*0.7)
        elif self.object.wam_34_p2 == 'C':
            table_data.append(0.14*0.5)
        elif self.object.wam_34_p2 == 'B':
            table_data.append(0.14*0.3)
        else: # A o nulo
            table_data.append(0.0)
       #wam 3.5
        if self.object.wam_35_act == 'E': 
            table_data.append(0.14*1.0)
        elif self.object.wam_35_act == 'D':
            table_data.append(0.14*0.7)
        elif self.object.wam_35_act == 'C':
            table_data.append(0.14*0.5)
        elif self.object.wam_35_act == 'B':
            table_data.append(0.14*0.3)
        else: # A o nulo
            table_data.append(0.0)

        if self.object.wam_35_p1 == 'E': 
            table_data.append(0.14*1.0)
        elif self.object.wam_35_p1 == 'D':
            table_data.append(0.14*0.7)
        elif self.object.wam_35_p1 == 'C':
            table_data.append(0.14*0.5)
        elif self.object.wam_35_p1 == 'B':
            table_data.append(0.14*0.3)
        else: # A o nulo
            table_data.append(0.0)
  
        if self.object.wam_35_p2 == 'E': 
            table_data.append(0.14*1.0)
        elif self.object.wam_35_p2 == 'D':
            table_data.append(0.14*0.7)
        elif self.object.wam_35_p2 == 'C':
            table_data.append(0.14*0.5)
        elif self.object.wam_35_p2 == 'B':
            table_data.append(0.14*0.3)
        else: # A o nulo
            table_data.append(0.0)
       #wam 3.6
        if self.object.wam_36_act == 'E': 
            table_data.append(0.14*1.0)
        elif self.object.wam_36_act == 'D':
            table_data.append(0.14*0.7)
        elif self.object.wam_36_act == 'C':
            table_data.append(0.14*0.4)
        elif self.object.wam_36_act == 'B':
            table_data.append(0.14*0.2)
        else: # A o nulo
            table_data.append(0.0)

        if self.object.wam_36_p1 == 'E': 
            table_data.append(0.14*1.0)
        elif self.object.wam_36_p1 == 'D':
            table_data.append(0.14*0.7)
        elif self.object.wam_36_p1 == 'C':
            table_data.append(0.14*0.4)
        elif self.object.wam_36_p1 == 'B':
            table_data.append(0.14*0.2)
        else: # A o nulo
            table_data.append(0.0)
  
        if self.object.wam_36_p2 == 'E': 
            table_data.append(0.14*1.0)
        elif self.object.wam_36_p2 == 'D':
            table_data.append(0.14*0.7)
        elif self.object.wam_36_p2 == 'C':
            table_data.append(0.14*0.4)
        elif self.object.wam_36_p2 == 'B':
            table_data.append(0.14*0.2)
        else: # A o nulo
            table_data.append(0.0)
       #wam 3.7
        if self.object.wam_37_act == 'E': 
            table_data.append(0.15*1.0)
        elif self.object.wam_37_act == 'D':
            table_data.append(0.15*0.7)
        elif self.object.wam_37_act == 'C':
            table_data.append(0.15*0.5)
        elif self.object.wam_37_act == 'B':
            table_data.append(0.15*0.3)
        else: # A o nulo
            table_data.append(0.0)

        if self.object.wam_37_p1 == 'E': 
            table_data.append(0.15*1.0)
        elif self.object.wam_37_p1 == 'D':
            table_data.append(0.15*0.7)
        elif self.object.wam_37_p1 == 'C':
            table_data.append(0.15*0.5)
        elif self.object.wam_37_p1 == 'B':
            table_data.append(0.15*0.3)
        else: # A o nulo
            table_data.append(0.0)
  
        if self.object.wam_37_p2 == 'E': 
            table_data.append(0.15*1.0)
        elif self.object.wam_37_p2 == 'D':
            table_data.append(0.15*0.7)
        elif self.object.wam_37_p2 == 'C':
            table_data.append(0.15*0.5)
        elif self.object.wam_37_p2 == 'B':
            table_data.append(0.15*0.3)
        else: # A o nulo
            table_data.append(0.0)
       #wam 4.1
        if self.object.wam_41_act == 'E': 
            table_data.append(0.25*1.0)
        elif self.object.wam_41_act == 'D':
            table_data.append(0.25*0.7)
        elif self.object.wam_41_act == 'C':
            table_data.append(0.25*0.4)
        elif self.object.wam_41_act == 'B':
            table_data.append(0.25*0.2)
        else: # A o nulo
            table_data.append(0.0)

        if self.object.wam_41_p1 == 'E': 
            table_data.append(0.25*1.0)
        elif self.object.wam_41_p1 == 'D':
            table_data.append(0.25*0.7)
        elif self.object.wam_41_p1 == 'C':
            table_data.append(0.25*0.4)
        elif self.object.wam_41_p1 == 'B':
            table_data.append(0.25*0.2)
        else: # A o nulo
            table_data.append(0.0)
  
        if self.object.wam_41_p2 == 'E': 
            table_data.append(0.25*1.0)
        elif self.object.wam_41_p2 == 'D':
            table_data.append(0.25*0.7)
        elif self.object.wam_41_p2 == 'C':
            table_data.append(0.25*0.4)
        elif self.object.wam_41_p2 == 'B':
            table_data.append(0.25*0.2)
        else: # A o nulo
            table_data.append(0.0)
       #wam 4.2
        if self.object.wam_42_act == 'E': 
            table_data.append(0.25*1.0)
        elif self.object.wam_42_act == 'D':
            table_data.append(0.25*0.7)
        elif self.object.wam_42_act == 'C':
            table_data.append(0.25*0.4)
        elif self.object.wam_42_act == 'B':
            table_data.append(0.25*0.2)
        else: # A o nulo
            table_data.append(0.0)

        if self.object.wam_42_p1 == 'E': 
            table_data.append(0.25*1.0)
        elif self.object.wam_42_p1 == 'D':
            table_data.append(0.25*0.7)
        elif self.object.wam_42_p1 == 'C':
            table_data.append(0.25*0.4)
        elif self.object.wam_42_p1 == 'B':
            table_data.append(0.25*0.2)
        else: # A o nulo
            table_data.append(0.0)
  
        if self.object.wam_42_p2 == 'E': 
            table_data.append(0.25*1.0)
        elif self.object.wam_42_p2 == 'D':
            table_data.append(0.25*0.7)
        elif self.object.wam_42_p2 == 'C':
            table_data.append(0.25*0.4)
        elif self.object.wam_42_p2 == 'B':
            table_data.append(0.25*0.2)
        else: # A o nulo
            table_data.append(0.0)
       #wam 4.3
        if self.object.wam_43_act == 'E': 
            table_data.append(0.25*1.0)
        elif self.object.wam_43_act == 'D':
            table_data.append(0.25*0.7)
        elif self.object.wam_43_act == 'C':
            table_data.append(0.25*0.4)
        elif self.object.wam_43_act == 'B':
            table_data.append(0.25*0.2)
        else: # A o nulo
            table_data.append(0.0)

        if self.object.wam_43_p1 == 'E': 
            table_data.append(0.25*1.0)
        elif self.object.wam_43_p1 == 'D':
            table_data.append(0.25*0.7)
        elif self.object.wam_43_p1 == 'C':
            table_data.append(0.25*0.4)
        elif self.object.wam_43_p1 == 'B':
            table_data.append(0.25*0.2)
        else: # A o nulo
            table_data.append(0.0)
  
        if self.object.wam_43_p2 == 'E': 
            table_data.append(0.25*1.0)
        elif self.object.wam_43_p2 == 'D':
            table_data.append(0.25*0.7)
        elif self.object.wam_43_p2 == 'C':
            table_data.append(0.25*0.4)
        elif self.object.wam_43_p2 == 'B':
            table_data.append(0.25*0.2)
        else: # A o nulo
            table_data.append(0.0)
       #wam 4.4
        if self.object.wam_44_act == 'E': 
            table_data.append(0.25*1.0)
        elif self.object.wam_44_act == 'D':
            table_data.append(0.25*0.7)
        elif self.object.wam_44_act == 'C':
            table_data.append(0.25*0.4)
        elif self.object.wam_44_act == 'B':
            table_data.append(0.25*0.2)
        else: # A o nulo
            table_data.append(0.0)

        if self.object.wam_44_p1 == 'E': 
            table_data.append(0.25*1.0)
        elif self.object.wam_44_p1 == 'D':
            table_data.append(0.25*0.7)
        elif self.object.wam_44_p1 == 'C':
            table_data.append(0.25*0.4)
        elif self.object.wam_44_p1 == 'B':
            table_data.append(0.25*0.2)
        else: # A o nulo
            table_data.append(0.0)
  
        if self.object.wam_44_p2 == 'E': 
            table_data.append(0.25*1.0)
        elif self.object.wam_44_p2 == 'D':
            table_data.append(0.25*0.7)
        elif self.object.wam_44_p2 == 'C':
            table_data.append(0.25*0.4)
        elif self.object.wam_44_p2 == 'B':
            table_data.append(0.25*0.2)
        else: # A o nulo
            table_data.append(0.0)
       #wam 5.1
        if self.object.wam_51_act == 'E': 
            table_data.append(0.5*1.0)
        elif self.object.wam_51_act == 'D':
            table_data.append(0.5*0.7)
        elif self.object.wam_51_act == 'C':
            table_data.append(0.5*0.3)
        elif self.object.wam_51_act == 'B':
            table_data.append(0.5*0.1)
        else: # A o nulo
            table_data.append(0.0)

        if self.object.wam_51_p1 == 'E': 
            table_data.append(0.5*1.0)
        elif self.object.wam_51_p1 == 'D':
            table_data.append(0.5*0.7)
        elif self.object.wam_51_p1 == 'C':
            table_data.append(0.5*0.3)
        elif self.object.wam_51_p1 == 'B':
            table_data.append(0.5*0.1)
        else: # A o nulo
            table_data.append(0.0)
  
        if self.object.wam_51_p2 == 'E': 
            table_data.append(0.5*1.0)
        elif self.object.wam_51_p2 == 'D':
            table_data.append(0.5*0.7)
        elif self.object.wam_51_p2 == 'C':
            table_data.append(0.5*0.3)
        elif self.object.wam_51_p2 == 'B':
            table_data.append(0.5*0.1)
        else: # A o nulo
            table_data.append(0.0)
       #wam 5.2
        if self.object.wam_52_act == 'E': 
            table_data.append(0.5*1.0)
        elif self.object.wam_52_act == 'D':
            table_data.append(0.5*0.7)
        elif self.object.wam_52_act == 'C':
            table_data.append(0.5*0.3)
        elif self.object.wam_52_act == 'B':
            table_data.append(0.5*0.1)
        else: # A o nulo
            table_data.append(0.0)

        if self.object.wam_52_p1 == 'E': 
            table_data.append(0.5*1.0)
        elif self.object.wam_52_p1 == 'D':
            table_data.append(0.5*0.7)
        elif self.object.wam_52_p1 == 'C':
            table_data.append(0.5*0.3)
        elif self.object.wam_52_p1 == 'B':
            table_data.append(0.5*0.1)
        else: # A o nulo
            table_data.append(0.0)
  
        if self.object.wam_52_p2 == 'E': 
            table_data.append(0.5*1.0)
        elif self.object.wam_52_p2 == 'D':
            table_data.append(0.5*0.7)
        elif self.object.wam_52_p2 == 'C':
            table_data.append(0.5*0.3)
        elif self.object.wam_52_p2 == 'B':
            table_data.append(0.5*0.1)
        else: # A o nulo
            table_data.append(0.0)

        return table_data

    def get_table_data_tech(self):
        table_data = [] #lista vacia para almacenar resultados 
        #############TECH#################
                #tech 1.1
        if self.object.tech_11_act == 'D': 
            table_data.append(0.2*1.0)
        elif self.object.tech_11_act == 'C':
            table_data.append(0.2*0.7)
        elif self.object.tech_11_act == 'B':
            table_data.append(0.2*0.5)
        else: # A o nulo
            table_data.append(0.0)

        if self.object.tech_11_p1 == 'D': 
            table_data.append(0.2*1.0)
        elif self.object.tech_11_p1 == 'C':
            table_data.append(0.2*0.7)
        elif self.object.tech_11_p1 == 'B':
            table_data.append(0.2*0.5)
        else: # A o nulo
            table_data.append(0.0)
  
        if self.object.tech_11_p2 == 'D': 
            table_data.append(0.2*1.0)
        elif self.object.tech_11_p2 == 'C':
            table_data.append(0.2*0.7)
        elif self.object.tech_11_p2 == 'B':
            table_data.append(0.2*0.5)
        else: # A o nulo
            table_data.append(0.0)
        #tech 1.2
        if self.object.tech_12_act == 'D': 
            table_data.append(0.2*1.0)
        elif self.object.tech_12_act == 'C':
            table_data.append(0.2*0.7)
        elif self.object.tech_12_act == 'B':
            table_data.append(0.2*0.5)
        else: # A o nulo
            table_data.append(0.0)

        if self.object.tech_12_p1 == 'D': 
            table_data.append(0.2*1.0)
        elif self.object.tech_12_p1 == 'C':
            table_data.append(0.2*0.7)
        elif self.object.tech_12_p1 == 'B':
            table_data.append(0.2*0.5)
        else: # A o nulo
            table_data.append(0.0)
  
        if self.object.tech_12_p2 == 'D': 
            table_data.append(0.2*1.0)
        elif self.object.tech_12_p2 == 'C':
            table_data.append(0.2*0.7)
        elif self.object.tech_12_p2 == 'B':
            table_data.append(0.2*0.5)
        else: # A o nulo
            table_data.append(0.0)
       #tech 1.3
        if self.object.tech_13_act == 'E': 
            table_data.append(0.2*1.0)
        elif self.object.tech_13_act == 'D':
            table_data.append(0.2*0.7)
        elif self.object.tech_13_act == 'C':
            table_data.append(0.2*0.5)
        elif self.object.tech_13_act == 'B':
            table_data.append(0.2*0.3)
        else: # A o nulo
            table_data.append(0.0)

        if self.object.tech_13_p1 == 'E': 
            table_data.append(0.2*1.0)
        elif self.object.tech_13_p1 == 'D':
            table_data.append(0.2*0.7)
        elif self.object.tech_13_p1 == 'C':
            table_data.append(0.2*0.5)
        elif self.object.tech_13_p1 == 'B':
            table_data.append(0.2*0.3)
        else: # A o nulo
            table_data.append(0.0)
  
        if self.object.tech_13_p2 == 'E': 
            table_data.append(0.2*1.0)
        elif self.object.tech_13_p2 == 'D':
            table_data.append(0.2*0.7)
        elif self.object.tech_13_p2 == 'C':
            table_data.append(0.2*0.5)
        elif self.object.tech_13_p2 == 'B':
            table_data.append(0.2*0.3)
        else: # A o nulo
            table_data.append(0.0)
        #tech 1.4
        if self.object.tech_14_act == 'D': 
            table_data.append(0.2*1.0)
        elif self.object.tech_14_act == 'C':
            table_data.append(0.2*0.9)
        elif self.object.tech_14_act == 'B':
            table_data.append(0.2*0.5)
        else: # A o nulo
            table_data.append(0.0)

        if self.object.tech_14_p1 == 'D': 
            table_data.append(0.2*1.0)
        elif self.object.tech_14_p1 == 'C':
            table_data.append(0.2*0.9)
        elif self.object.tech_14_p1 == 'B':
            table_data.append(0.2*0.5)
        else: # A o nulo
            table_data.append(0.0)
  
        if self.object.tech_14_p2 == 'D': 
            table_data.append(0.2*1.0)
        elif self.object.tech_14_p2 == 'C':
            table_data.append(0.2*0.9)
        elif self.object.tech_14_p2 == 'B':
            table_data.append(0.2*0.5)
        else: # A o nulo
            table_data.append(0.0)
       #tech 1.5
        if self.object.tech_15_act == 'E': 
            table_data.append(0.2*1.0)
        elif self.object.tech_15_act == 'D':
            table_data.append(0.2*0.7)
        elif self.object.tech_15_act == 'C':
            table_data.append(0.2*0.5)
        elif self.object.tech_15_act == 'B':
            table_data.append(0.2*0.3)
        else: # A o nulo
            table_data.append(0.0)

        if self.object.tech_15_p1 == 'E': 
            table_data.append(0.2*1.0)
        elif self.object.tech_15_p1 == 'D':
            table_data.append(0.2*0.7)
        elif self.object.tech_15_p1 == 'C':
            table_data.append(0.2*0.5)
        elif self.object.tech_15_p1 == 'B':
            table_data.append(0.2*0.3)
        else: # A o nulo
            table_data.append(0.0)
  
        if self.object.tech_15_p2 == 'E': 
            table_data.append(0.2*1.0)
        elif self.object.tech_15_p2 == 'D':
            table_data.append(0.2*0.7)
        elif self.object.tech_15_p2 == 'C':
            table_data.append(0.2*0.5)
        elif self.object.tech_15_p2 == 'B':
            table_data.append(0.2*0.3)
        else: # A o nulo
            table_data.append(0.0)
        #tech 2.1
        if self.object.tech_21_act == 'D': 
            table_data.append(0.16*1.0)
        elif self.object.tech_21_act == 'C':
            table_data.append(0.16*0.7)
        elif self.object.tech_21_act == 'B':
            table_data.append(0.16*0.5)
        else: # A o nulo
            table_data.append(0.0)

        if self.object.tech_21_p1 == 'D': 
            table_data.append(0.16*1.0)
        elif self.object.tech_21_p1 == 'C':
            table_data.append(0.16*0.7)
        elif self.object.tech_21_p1 == 'B':
            table_data.append(0.16*0.5)
        else: # A o nulo
            table_data.append(0.0)
  
        if self.object.tech_21_p2 == 'D': 
            table_data.append(0.16*1.0)
        elif self.object.tech_21_p2 == 'C':
            table_data.append(0.16*0.7)
        elif self.object.tech_21_p2 == 'B':
            table_data.append(0.16*0.5)
        else: # A o nulo
            table_data.append(0.0)
       #tech 2.2
        if self.object.tech_22_act == 'E': 
            table_data.append(0.16*1.0)
        elif self.object.tech_22_act == 'D':
            table_data.append(0.16*0.7)
        elif self.object.tech_22_act == 'C':
            table_data.append(0.16*0.5)
        elif self.object.tech_22_act == 'B':
            table_data.append(0.16*0.3)
        else: # A o nulo
            table_data.append(0.0)

        if self.object.tech_22_p1 == 'E': 
            table_data.append(0.16*1.0)
        elif self.object.tech_22_p1 == 'D':
            table_data.append(0.16*0.7)
        elif self.object.tech_22_p1 == 'C':
            table_data.append(0.16*0.5)
        elif self.object.tech_22_p1 == 'B':
            table_data.append(0.16*0.3)
        else: # A o nulo
            table_data.append(0.0)
  
        if self.object.tech_22_p2 == 'E': 
            table_data.append(0.16*1.0)
        elif self.object.tech_22_p2 == 'D':
            table_data.append(0.16*0.7)
        elif self.object.tech_22_p2 == 'C':
            table_data.append(0.16*0.5)
        elif self.object.tech_22_p2 == 'B':
            table_data.append(0.16*0.3)
        else: # A o nulo
            table_data.append(0.0)
        #tech 2.3
        if self.object.tech_23_act == 'D': 
            table_data.append(0.16*1.0)
        elif self.object.tech_23_act == 'C':
            table_data.append(0.16*0.7)
        elif self.object.tech_23_act == 'B':
            table_data.append(0.16*0.5)
        else: # A o nulo
            table_data.append(0.0)

        if self.object.tech_23_p1 == 'D': 
            table_data.append(0.16*1.0)
        elif self.object.tech_23_p1 == 'C':
            table_data.append(0.16*0.7)
        elif self.object.tech_23_p1 == 'B':
            table_data.append(0.16*0.5)
        else: # A o nulo
            table_data.append(0.0)
  
        if self.object.tech_23_p2 == 'D': 
            table_data.append(0.16*1.0)
        elif self.object.tech_23_p2 == 'C':
            table_data.append(0.16*0.7)
        elif self.object.tech_23_p2 == 'B':
            table_data.append(0.16*0.5)
        else: # A o nulo
            table_data.append(0.0)
        #tech 2.4
        if self.object.tech_24_act == 'D': 
            table_data.append(0.12*1.0)
        elif self.object.tech_24_act == 'C':
            table_data.append(0.12*0.7)
        elif self.object.tech_24_act == 'B':
            table_data.append(0.12*0.5)
        else: # A o nulo
            table_data.append(0.0)

        if self.object.tech_24_p1 == 'D': 
            table_data.append(0.12*1.0)
        elif self.object.tech_24_p1 == 'C':
            table_data.append(0.12*0.7)
        elif self.object.tech_24_p1 == 'B':
            table_data.append(0.12*0.5)
        else: # A o nulo
            table_data.append(0.0)
  
        if self.object.tech_24_p2 == 'D': 
            table_data.append(0.12*1.0)
        elif self.object.tech_24_p2 == 'C':
            table_data.append(0.12*0.7)
        elif self.object.tech_24_p2 == 'B':
            table_data.append(0.12*0.5)
        else: # A o nulo
            table_data.append(0.0)
       #tech 2.5
        if self.object.tech_25_act == 'E': 
            table_data.append(0.16*1.0)
        elif self.object.tech_25_act == 'D':
            table_data.append(0.16*0.7)
        elif self.object.tech_25_act == 'C':
            table_data.append(0.16*0.5)
        elif self.object.tech_25_act == 'B':
            table_data.append(0.16*0.3)
        else: # A o nulo
            table_data.append(0.0)

        if self.object.tech_25_p1 == 'E': 
            table_data.append(0.16*1.0)
        elif self.object.tech_25_p1 == 'D':
            table_data.append(0.16*0.7)
        elif self.object.tech_25_p1 == 'C':
            table_data.append(0.16*0.5)
        elif self.object.tech_25_p1 == 'B':
            table_data.append(0.16*0.3)
        else: # A o nulo
            table_data.append(0.0)
  
        if self.object.tech_25_p2 == 'E': 
            table_data.append(0.16*1.0)
        elif self.object.tech_25_p2 == 'D':
            table_data.append(0.16*0.7)
        elif self.object.tech_25_p2 == 'C':
            table_data.append(0.16*0.5)
        elif self.object.tech_25_p2 == 'B':
            table_data.append(0.16*0.3)
        else: # A o nulo
            table_data.append(0.0)
       #tech 2.6
        if self.object.tech_26_act == 'E': 
            table_data.append(0.12*1.0)
        elif self.object.tech_26_act == 'D':
            table_data.append(0.12*0.7)
        elif self.object.tech_26_act == 'C':
            table_data.append(0.12*0.3)
        elif self.object.tech_26_act == 'B':
            table_data.append(0.12*0.0)
        else: # A o nulo
            table_data.append(0.0)

        if self.object.tech_26_p1 == 'E': 
            table_data.append(0.12*1.0)
        elif self.object.tech_26_p1 == 'D':
            table_data.append(0.12*0.7)
        elif self.object.tech_26_p1 == 'C':
            table_data.append(0.12*0.3)
        elif self.object.tech_26_p1 == 'B':
            table_data.append(0.12*0.0)
        else: # A o nulo
            table_data.append(0.0)
  
        if self.object.tech_26_p2 == 'E': 
            table_data.append(0.12*1.0)
        elif self.object.tech_26_p2 == 'D':
            table_data.append(0.12*0.7)
        elif self.object.tech_26_p2 == 'C':
            table_data.append(0.12*0.3)
        elif self.object.tech_26_p2 == 'B':
            table_data.append(0.12*0.0)
        else: # A o nulo
            table_data.append(0.0)
       #tech 2.7
        if self.object.tech_27_act == 'E': 
            table_data.append(0.12*1.0)
        elif self.object.tech_27_act == 'D':
            table_data.append(0.12*0.7)
        elif self.object.tech_27_act == 'C':
            table_data.append(0.12*0.5)
        elif self.object.tech_27_act == 'B':
            table_data.append(0.12*0.3)
        else: # A o nulo
            table_data.append(0.0)

        if self.object.tech_27_p1 == 'E': 
            table_data.append(0.12*1.0)
        elif self.object.tech_27_p1 == 'D':
            table_data.append(0.12*0.7)
        elif self.object.tech_27_p1 == 'C':
            table_data.append(0.12*0.5)
        elif self.object.tech_27_p1 == 'B':
            table_data.append(0.12*0.3)
        else: # A o nulo
            table_data.append(0.0)
  
        if self.object.tech_27_p2 == 'E': 
            table_data.append(0.12*1.0)
        elif self.object.tech_27_p2 == 'D':
            table_data.append(0.12*0.7)
        elif self.object.tech_27_p2 == 'C':
            table_data.append(0.12*0.5)
        elif self.object.tech_27_p2 == 'B':
            table_data.append(0.12*0.3)
        else: # A o nulo
            table_data.append(0.0)
       #tech 3.1
        if self.object.tech_31_act == 'E': 
            table_data.append(0.17*1.0)
        elif self.object.tech_31_act == 'D':
            table_data.append(0.17*0.7)
        elif self.object.tech_31_act == 'C':
            table_data.append(0.17*0.5)
        elif self.object.tech_31_act == 'B':
            table_data.append(0.17*0.3)
        else: # A o nulo
            table_data.append(0.0)

        if self.object.tech_31_p1 == 'E': 
            table_data.append(0.17*1.0)
        elif self.object.tech_31_p1 == 'D':
            table_data.append(0.17*0.7)
        elif self.object.tech_31_p1 == 'C':
            table_data.append(0.17*0.5)
        elif self.object.tech_31_p1 == 'B':
            table_data.append(0.17*0.3)
        else: # A o nulo
            table_data.append(0.0)
  
        if self.object.tech_31_p2 == 'E': 
            table_data.append(0.17*1.0)
        elif self.object.tech_31_p2 == 'D':
            table_data.append(0.17*0.7)
        elif self.object.tech_31_p2 == 'C':
            table_data.append(0.17*0.5)
        elif self.object.tech_31_p2 == 'B':
            table_data.append(0.17*0.3)
        else: # A o nulo
            table_data.append(0.0)
       #tech 3.2
        if self.object.tech_32_act == 'E': 
            table_data.append(0.17*1.0)
        elif self.object.tech_32_act == 'D':
            table_data.append(0.17*0.7)
        elif self.object.tech_32_act == 'C':
            table_data.append(0.17*0.5)
        elif self.object.tech_32_act == 'B':
            table_data.append(0.17*0.3)
        else: # A o nulo
            table_data.append(0.0)

        if self.object.tech_32_p1 == 'E': 
            table_data.append(0.17*1.0)
        elif self.object.tech_32_p1 == 'D':
            table_data.append(0.17*0.7)
        elif self.object.tech_32_p1 == 'C':
            table_data.append(0.17*0.5)
        elif self.object.tech_32_p1 == 'B':
            table_data.append(0.17*0.3)
        else: # A o nulo
            table_data.append(0.0)
  
        if self.object.tech_32_p2 == 'E': 
            table_data.append(0.17*1.0)
        elif self.object.tech_32_p2 == 'D':
            table_data.append(0.17*0.7)
        elif self.object.tech_32_p2 == 'C':
            table_data.append(0.17*0.5)
        elif self.object.tech_32_p2 == 'B':
            table_data.append(0.17*0.3)
        else: # A o nulo
            table_data.append(0.0)
       #tech 3.3
        if self.object.tech_33_act == 'E': 
            table_data.append(0.17*1.0)
        elif self.object.tech_33_act == 'D':
            table_data.append(0.17*0.7)
        elif self.object.tech_33_act == 'C':
            table_data.append(0.17*0.5)
        elif self.object.tech_33_act == 'B':
            table_data.append(0.17*0.3)
        else: # A o nulo
            table_data.append(0.0)

        if self.object.tech_33_p1 == 'E': 
            table_data.append(0.17*1.0)
        elif self.object.tech_33_p1 == 'D':
            table_data.append(0.17*0.7)
        elif self.object.tech_33_p1 == 'C':
            table_data.append(0.17*0.5)
        elif self.object.tech_33_p1 == 'B':
            table_data.append(0.17*0.3)
        else: # A o nulo
            table_data.append(0.0)
  
        if self.object.tech_33_p2 == 'E': 
            table_data.append(0.17*1.0)
        elif self.object.tech_33_p2 == 'D':
            table_data.append(0.17*0.7)
        elif self.object.tech_33_p2 == 'C':
            table_data.append(0.17*0.5)
        elif self.object.tech_33_p2 == 'B':
            table_data.append(0.17*0.3)
        else: # A o nulo
            table_data.append(0.0)
       #tech 3.4
        if self.object.tech_34_act == 'E': 
            table_data.append(0.15*1.0)
        elif self.object.tech_34_act == 'D':
            table_data.append(0.15*0.7)
        elif self.object.tech_34_act == 'C':
            table_data.append(0.15*0.5)
        elif self.object.tech_34_act == 'B':
            table_data.append(0.15*0.3)
        else: # A o nulo
            table_data.append(0.0)

        if self.object.tech_34_p1 == 'E': 
            table_data.append(0.15*1.0)
        elif self.object.tech_34_p1 == 'D':
            table_data.append(0.15*0.7)
        elif self.object.tech_34_p1 == 'C':
            table_data.append(0.15*0.5)
        elif self.object.tech_34_p1 == 'B':
            table_data.append(0.15*0.3)
        else: # A o nulo
            table_data.append(0.0)
  
        if self.object.tech_34_p2 == 'E': 
            table_data.append(0.15*1.0)
        elif self.object.tech_34_p2 == 'D':
            table_data.append(0.15*0.7)
        elif self.object.tech_34_p2 == 'C':
            table_data.append(0.15*0.5)
        elif self.object.tech_34_p2 == 'B':
            table_data.append(0.15*0.3)
        else: # A o nulo
            table_data.append(0.0)
       #tech 3.5
        if self.object.tech_35_act == 'E': 
            table_data.append(0.17*1.0)
        elif self.object.tech_35_act == 'D':
            table_data.append(0.17*0.7)
        elif self.object.tech_35_act == 'C':
            table_data.append(0.17*0.5)
        elif self.object.tech_35_act == 'B':
            table_data.append(0.17*0.3)
        else: # A o nulo
            table_data.append(0.0)

        if self.object.tech_35_p1 == 'E': 
            table_data.append(0.17*1.0)
        elif self.object.tech_35_p1 == 'D':
            table_data.append(0.17*0.7)
        elif self.object.tech_35_p1 == 'C':
            table_data.append(0.17*0.5)
        elif self.object.tech_35_p1 == 'B':
            table_data.append(0.17*0.3)
        else: # A o nulo
            table_data.append(0.0)
  
        if self.object.tech_35_p2 == 'E': 
            table_data.append(0.17*1.0)
        elif self.object.tech_35_p2 == 'D':
            table_data.append(0.17*0.7)
        elif self.object.tech_35_p2 == 'C':
            table_data.append(0.17*0.5)
        elif self.object.tech_35_p2 == 'B':
            table_data.append(0.17*0.3)
        else: # A o nulo
            table_data.append(0.0)
       #tech 3.6
        if self.object.tech_36_act == 'E': 
            table_data.append(0.17*1.0)
        elif self.object.tech_36_act == 'D':
            table_data.append(0.17*0.7)
        elif self.object.tech_36_act == 'C':
            table_data.append(0.17*0.5)
        elif self.object.tech_36_act == 'B':
            table_data.append(0.17*0.3)
        else: # A o nulo
            table_data.append(0.0)

        if self.object.tech_36_p1 == 'E': 
            table_data.append(0.17*1.0)
        elif self.object.tech_36_p1 == 'D':
            table_data.append(0.17*0.7)
        elif self.object.tech_36_p1 == 'C':
            table_data.append(0.17*0.5)
        elif self.object.tech_36_p1 == 'B':
            table_data.append(0.17*0.3)
        else: # A o nulo
            table_data.append(0.0)
  
        if self.object.tech_36_p2 == 'E': 
            table_data.append(0.17*1.0)
        elif self.object.tech_36_p2 == 'D':
            table_data.append(0.17*0.7)
        elif self.object.tech_36_p2 == 'C':
            table_data.append(0.17*0.5)
        elif self.object.tech_36_p2 == 'B':
            table_data.append(0.17*0.3)
        else: # A o nulo
            table_data.append(0.0)
       #tech 4.1
        if self.object.tech_41_act == 'E': 
            table_data.append(0.17*1.0)
        elif self.object.tech_41_act == 'D':
            table_data.append(0.17*0.7)
        elif self.object.tech_41_act == 'C':
            table_data.append(0.17*0.5)
        elif self.object.tech_41_act == 'B':
            table_data.append(0.17*0.3)
        else: # A o nulo
            table_data.append(0.0)

        if self.object.tech_41_p1 == 'E': 
            table_data.append(0.17*1.0)
        elif self.object.tech_41_p1 == 'D':
            table_data.append(0.17*0.7)
        elif self.object.tech_41_p1 == 'C':
            table_data.append(0.17*0.5)
        elif self.object.tech_41_p1 == 'B':
            table_data.append(0.17*0.3)
        else: # A o nulo
            table_data.append(0.0)
  
        if self.object.tech_41_p2 == 'E': 
            table_data.append(0.17*1.0)
        elif self.object.tech_41_p2 == 'D':
            table_data.append(0.17*0.7)
        elif self.object.tech_41_p2 == 'C':
            table_data.append(0.17*0.5)
        elif self.object.tech_41_p2 == 'B':
            table_data.append(0.17*0.3)
        else: # A o nulo
            table_data.append(0.0)
       #tech 4.2
        if self.object.tech_42_act == 'E': 
            table_data.append(0.15*1.0)
        elif self.object.tech_42_act == 'D':
            table_data.append(0.15*0.7)
        elif self.object.tech_42_act == 'C':
            table_data.append(0.15*0.5)
        elif self.object.tech_42_act == 'B':
            table_data.append(0.15*0.3)
        else: # A o nulo
            table_data.append(0.0)

        if self.object.tech_42_p1 == 'E': 
            table_data.append(0.15*1.0)
        elif self.object.tech_42_p1 == 'D':
            table_data.append(0.15*0.7)
        elif self.object.tech_42_p1 == 'C':
            table_data.append(0.15*0.5)
        elif self.object.tech_42_p1 == 'B':
            table_data.append(0.15*0.3)
        else: # A o nulo
            table_data.append(0.0)
  
        if self.object.tech_42_p2 == 'E': 
            table_data.append(0.15*1.0)
        elif self.object.tech_42_p2 == 'D':
            table_data.append(0.15*0.7)
        elif self.object.tech_42_p2 == 'C':
            table_data.append(0.15*0.5)
        elif self.object.tech_42_p2 == 'B':
            table_data.append(0.15*0.3)
        else: # A o nulo
            table_data.append(0.0)
       #tech 4.3
        if self.object.tech_43_act == 'E': 
            table_data.append(0.19*1.0)
        elif self.object.tech_43_act == 'D':
            table_data.append(0.19*0.7)
        elif self.object.tech_43_act == 'C':
            table_data.append(0.19*0.5)
        elif self.object.tech_43_act == 'B':
            table_data.append(0.19*0.3)
        else: # A o nulo
            table_data.append(0.0)

        if self.object.tech_43_p1 == 'E': 
            table_data.append(0.19*1.0)
        elif self.object.tech_43_p1 == 'D':
            table_data.append(0.19*0.7)
        elif self.object.tech_43_p1 == 'C':
            table_data.append(0.19*0.5)
        elif self.object.tech_43_p1 == 'B':
            table_data.append(0.19*0.3)
        else: # A o nulo
            table_data.append(0.0)
  
        if self.object.tech_43_p2 == 'E': 
            table_data.append(0.19*1.0)
        elif self.object.tech_43_p2 == 'D':
            table_data.append(0.19*0.7)
        elif self.object.tech_43_p2 == 'C':
            table_data.append(0.19*0.5)
        elif self.object.tech_43_p2 == 'B':
            table_data.append(0.19*0.3)
        else: # A o nulo
            table_data.append(0.0)
        #tech 4.4
        if self.object.tech_44_act == 'F': 
            table_data.append(0.15*1.0)
        elif self.object.tech_44_act == 'E':
            table_data.append(0.15*0.7)
        elif self.object.tech_44_act == 'D':
            table_data.append(0.15*0.5)
        elif self.object.tech_44_act == 'C':
            table_data.append(0.15*0.3)
        elif self.object.tech_44_act == 'B':
            table_data.append(0.15*0.3)
        else: # A o nulo
            table_data.append(0.0)

        if self.object.tech_44_p1 == 'F': 
            table_data.append(0.15*1.0)
        elif self.object.tech_44_p1 == 'E':
            table_data.append(0.15*0.7)
        elif self.object.tech_44_p1 == 'D':
            table_data.append(0.15*0.5)
        elif self.object.tech_44_p1 == 'C':
            table_data.append(0.15*0.3)
        elif self.object.tech_44_p1 == 'B':
            table_data.append(0.15*0.3)
        else: # A o nulo
            table_data.append(0.0)
  
        if self.object.tech_44_p2 == 'F': 
            table_data.append(0.15*1.0)
        elif self.object.tech_44_p2 == 'E':
            table_data.append(0.15*0.7)
        elif self.object.tech_44_p2 == 'D':
            table_data.append(0.15*0.5)
        elif self.object.tech_44_p2 == 'C':
            table_data.append(0.15*0.3)
        elif self.object.tech_44_p2 == 'B':
            table_data.append(0.15*0.3)
        else: # A o nulo
            table_data.append(0.0)
        #tech 4.5
        if self.object.tech_45_act == 'D': 
            table_data.append(0.19*1.0)
        elif self.object.tech_45_act == 'C':
            table_data.append(0.19*0.7)
        elif self.object.tech_45_act == 'B':
            table_data.append(0.19*0.5)
        else: # A o nulo
            table_data.append(0.0)

        if self.object.tech_45_p1 == 'D': 
            table_data.append(0.19*1.0)
        elif self.object.tech_45_p1 == 'C':
            table_data.append(0.19*0.7)
        elif self.object.tech_45_p1 == 'B':
            table_data.append(0.19*0.5)
        else: # A o nulo
            table_data.append(0.0)
  
        if self.object.tech_45_p2 == 'D': 
            table_data.append(0.19*1.0)
        elif self.object.tech_45_p2 == 'C':
            table_data.append(0.19*0.7)
        elif self.object.tech_45_p2 == 'B':
            table_data.append(0.19*0.5)
        else: # A o nulo
            table_data.append(0.0)
        #tech 4.6
        if self.object.tech_46_act == 'D': 
            table_data.append(0.15*1.0)
        elif self.object.tech_46_act == 'C':
            table_data.append(0.15*0.7)
        elif self.object.tech_46_act == 'B':
            table_data.append(0.15*0.5)
        else: # A o nulo
            table_data.append(0.0)

        if self.object.tech_46_p1 == 'D': 
            table_data.append(0.15*1.0)
        elif self.object.tech_46_p1 == 'C':
            table_data.append(0.15*0.7)
        elif self.object.tech_46_p1 == 'B':
            table_data.append(0.15*0.5)
        else: # A o nulo
            table_data.append(0.0)
  
        if self.object.tech_46_p2 == 'D': 
            table_data.append(0.15*1.0)
        elif self.object.tech_46_p2 == 'C':
            table_data.append(0.15*0.7)
        elif self.object.tech_46_p2 == 'B':
            table_data.append(0.15*0.5)
        else: # A o nulo
            table_data.append(0.0)
        #tech 5.1
        if self.object.tech_51_act == 'D': 
            table_data.append(0.4*1.0)
        elif self.object.tech_51_act == 'C':
            table_data.append(0.4*0.5)
        elif self.object.tech_51_act == 'B':
            table_data.append(0.4*0.3)
        else: # A o nulo
            table_data.append(0.0)

        if self.object.tech_51_p1 == 'D': 
            table_data.append(0.4*1.0)
        elif self.object.tech_51_p1 == 'C':
            table_data.append(0.4*0.5)
        elif self.object.tech_51_p1 == 'B':
            table_data.append(0.4*0.3)
        else: # A o nulo
            table_data.append(0.0)
  
        if self.object.tech_51_p2 == 'D': 
            table_data.append(0.4*1.0)
        elif self.object.tech_51_p2 == 'C':
            table_data.append(0.4*0.5)
        elif self.object.tech_51_p2 == 'B':
            table_data.append(0.4*0.3)
        else: # A o nulo
            table_data.append(0.0)
       #tech 5.2
        if self.object.tech_52_act == 'E': 
            table_data.append(0.6*1.0)
        elif self.object.tech_52_act == 'D':
            table_data.append(0.6*0.7)
        elif self.object.tech_52_act == 'C':
            table_data.append(0.6*0.5)
        elif self.object.tech_52_act == 'B':
            table_data.append(0.6*0.3)
        else: # A o nulo
            table_data.append(0.0)

        if self.object.tech_52_p1 == 'E': 
            table_data.append(0.6*1.0)
        elif self.object.tech_52_p1 == 'D':
            table_data.append(0.6*0.7)
        elif self.object.tech_52_p1 == 'C':
            table_data.append(0.6*0.5)
        elif self.object.tech_52_p1 == 'B':
            table_data.append(0.6*0.3)
        else: # A o nulo
            table_data.append(0.0)
  
        if self.object.tech_52_p2 == 'E': 
            table_data.append(0.6*1.0)
        elif self.object.tech_52_p2 == 'D':
            table_data.append(0.6*0.7)
        elif self.object.tech_52_p2 == 'C':
            table_data.append(0.6*0.5)
        elif self.object.tech_52_p2 == 'B':
            table_data.append(0.6*0.3)
        else: # A o nulo
            table_data.append(0.0)

        return table_data

    def get_table_data_cust(self):
        table_data = [] #lista vacia para almacenar resultados 
        #############CUST#################
                #cust 1.1
        if self.object.cust_11_act == 'D': 
            table_data.append(0.25*1.0)
        elif self.object.cust_11_act == 'C':
            table_data.append(0.25*0.7)
        elif self.object.cust_11_act == 'B':
            table_data.append(0.25*0.5)
        else: # A o nulo
            table_data.append(0.0)

        if self.object.cust_11_p1 == 'D': 
            table_data.append(0.25*1.0)
        elif self.object.cust_11_p1 == 'C':
            table_data.append(0.25*0.7)
        elif self.object.cust_11_p1 == 'B':
            table_data.append(0.25*0.5)
        else: # A o nulo
            table_data.append(0.0)
  
        if self.object.cust_11_p2 == 'D': 
            table_data.append(0.25*1.0)
        elif self.object.cust_11_p2 == 'C':
            table_data.append(0.25*0.7)
        elif self.object.cust_11_p2 == 'B':
            table_data.append(0.25*0.5)
        else: # A o nulo
            table_data.append(0.0)
        #cust 1.2
        if self.object.cust_12_act == 'D': 
            table_data.append(0.25*1.0)
        elif self.object.cust_12_act == 'C':
            table_data.append(0.25*0.7)
        elif self.object.cust_12_act == 'B':
            table_data.append(0.25*0.5)
        else: # A o nulo
            table_data.append(0.0)

        if self.object.cust_12_p1 == 'D': 
            table_data.append(0.25*1.0)
        elif self.object.cust_12_p1 == 'C':
            table_data.append(0.25*0.7)
        elif self.object.cust_12_p1 == 'B':
            table_data.append(0.25*0.5)
        else: # A o nulo
            table_data.append(0.0)
  
        if self.object.cust_12_p2 == 'D': 
            table_data.append(0.25*1.0)
        elif self.object.cust_12_p2 == 'C':
            table_data.append(0.25*0.7)
        elif self.object.cust_12_p2 == 'B':
            table_data.append(0.25*0.5)
        else: # A o nulo
            table_data.append(0.0)
        #cust 1.3
        if self.object.cust_13_act == 'D': 
            table_data.append(0.25*1.0)
        elif self.object.cust_13_act == 'C':
            table_data.append(0.25*0.7)
        elif self.object.cust_13_act == 'B':
            table_data.append(0.25*0.5)
        else: # A o nulo
            table_data.append(0.0)

        if self.object.cust_13_p1 == 'D': 
            table_data.append(0.25*1.0)
        elif self.object.cust_13_p1 == 'C':
            table_data.append(0.25*0.7)
        elif self.object.cust_13_p1 == 'B':
            table_data.append(0.25*0.5)
        else: # A o nulo
            table_data.append(0.0)
  
        if self.object.cust_13_p2 == 'D': 
            table_data.append(0.25*1.0)
        elif self.object.cust_13_p2 == 'C':
            table_data.append(0.25*0.7)
        elif self.object.cust_13_p2 == 'B':
            table_data.append(0.25*0.5)
        else: # A o nulo
            table_data.append(0.0)
        #cust 1.4
        if self.object.cust_14_act == 'C': 
            table_data.append(0.25*1.0)
        elif self.object.cust_14_act == 'B':
            table_data.append(0.25*0.5)
        else: # A o nulo
            table_data.append(0.0)

        if self.object.cust_14_p1 == 'C': 
            table_data.append(0.25*1.0)
        elif self.object.cust_14_p1 == 'B':
            table_data.append(0.25*0.5)
        else: # A o nulo
            table_data.append(0.0)
  
        if self.object.cust_14_p2 == 'C': 
            table_data.append(0.25*1.0)
        elif self.object.cust_14_p2 == 'B':
            table_data.append(0.25*0.5)
        else: # A o nulo
            table_data.append(0.0)
        #cust 2.1
        if self.object.cust_21_act == 'D': 
            table_data.append(0.17*1.0)
        elif self.object.cust_21_act == 'C':
            table_data.append(0.17*0.7)
        elif self.object.cust_21_act == 'B':
            table_data.append(0.17*0.3)
        else: # A o nulo
            table_data.append(0.0)

        if self.object.cust_21_p1 == 'D': 
            table_data.append(0.17*1.0)
        elif self.object.cust_21_p1 == 'C':
            table_data.append(0.17*0.7)
        elif self.object.cust_21_p1 == 'B':
            table_data.append(0.17*0.3)
        else: # A o nulo
            table_data.append(0.0)
  
        if self.object.cust_21_p2 == 'D': 
            table_data.append(0.17*1.0)
        elif self.object.cust_21_p2 == 'C':
            table_data.append(0.17*0.7)
        elif self.object.cust_21_p2 == 'B':
            table_data.append(0.17*0.3)
        else: # A o nulo
            table_data.append(0.0)
       #cust 2.2
        if self.object.cust_22_act == 'E': 
            table_data.append(0.17*1.0)
        elif self.object.cust_22_act == 'D':
            table_data.append(0.17*0.7)
        elif self.object.cust_22_act == 'C':
            table_data.append(0.17*0.5)
        elif self.object.cust_22_act == 'B':
            table_data.append(0.17*0.3)
        else: # A o nulo
            table_data.append(0.0)

        if self.object.cust_22_p1 == 'E': 
            table_data.append(0.17*1.0)
        elif self.object.cust_22_p1 == 'D':
            table_data.append(0.17*0.7)
        elif self.object.cust_22_p1 == 'C':
            table_data.append(0.17*0.5)
        elif self.object.cust_22_p1 == 'B':
            table_data.append(0.17*0.3)
        else: # A o nulo
            table_data.append(0.0)
  
        if self.object.cust_22_p2 == 'E': 
            table_data.append(0.17*1.0)
        elif self.object.cust_22_p2 == 'D':
            table_data.append(0.17*0.7)
        elif self.object.cust_22_p2 == 'C':
            table_data.append(0.17*0.5)
        elif self.object.cust_22_p2 == 'B':
            table_data.append(0.17*0.3)
        else: # A o nulo
            table_data.append(0.0)
       #cust 2.3
        if self.object.cust_23_act == 'E': 
            table_data.append(0.15*1.0)
        elif self.object.cust_23_act == 'D':
            table_data.append(0.15*0.7)
        elif self.object.cust_23_act == 'C':
            table_data.append(0.15*0.5)
        elif self.object.cust_23_act == 'B':
            table_data.append(0.15*0.3)
        else: # A o nulo
            table_data.append(0.0)

        if self.object.cust_23_p1 == 'E': 
            table_data.append(0.15*1.0)
        elif self.object.cust_23_p1 == 'D':
            table_data.append(0.15*0.7)
        elif self.object.cust_23_p1 == 'C':
            table_data.append(0.15*0.5)
        elif self.object.cust_23_p1 == 'B':
            table_data.append(0.15*0.3)
        else: # A o nulo
            table_data.append(0.0)
  
        if self.object.cust_23_p2 == 'E': 
            table_data.append(0.15*1.0)
        elif self.object.cust_23_p2 == 'D':
            table_data.append(0.15*0.7)
        elif self.object.cust_23_p2 == 'C':
            table_data.append(0.15*0.5)
        elif self.object.cust_23_p2 == 'B':
            table_data.append(0.15*0.3)
        else: # A o nulo
            table_data.append(0.0)
        #cust 2.4
        if self.object.cust_24_act == 'D': 
            table_data.append(0.17*1.0)
        elif self.object.cust_24_act == 'C':
            table_data.append(0.17*0.7)
        elif self.object.cust_24_act == 'B':
            table_data.append(0.17*0.3)
        else: # A o nulo
            table_data.append(0.0)

        if self.object.cust_24_p1 == 'D': 
            table_data.append(0.17*1.0)
        elif self.object.cust_24_p1 == 'C':
            table_data.append(0.17*0.7)
        elif self.object.cust_24_p1 == 'B':
            table_data.append(0.17*0.3)
        else: # A o nulo
            table_data.append(0.0)
  
        if self.object.cust_24_p2 == 'D': 
            table_data.append(0.17*1.0)
        elif self.object.cust_24_p2 == 'C':
            table_data.append(0.17*0.7)
        elif self.object.cust_24_p2 == 'B':
            table_data.append(0.17*0.3)
        else: # A o nulo
            table_data.append(0.0)
        #cust 2.5
        if self.object.cust_25_act == 'D': 
            table_data.append(0.17*1.0)
        elif self.object.cust_25_act == 'C':
            table_data.append(0.17*0.7)
        elif self.object.cust_25_act == 'B':
            table_data.append(0.17*0.3)
        else: # A o nulo
            table_data.append(0.0)

        if self.object.cust_25_p1 == 'D': 
            table_data.append(0.17*1.0)
        elif self.object.cust_25_p1 == 'C':
            table_data.append(0.17*0.7)
        elif self.object.cust_25_p1 == 'B':
            table_data.append(0.17*0.3)
        else: # A o nulo
            table_data.append(0.0)
  
        if self.object.cust_25_p2 == 'D': 
            table_data.append(0.17*1.0)
        elif self.object.cust_25_p2 == 'C':
            table_data.append(0.17*0.7)
        elif self.object.cust_25_p2 == 'B':
            table_data.append(0.17*0.3)
        else: # A o nulo
            table_data.append(0.0)
       #cust 2.6
        if self.object.cust_26_act == 'E': 
            table_data.append(0.17*1.0)
        elif self.object.cust_26_act == 'D':
            table_data.append(0.17*0.7)
        elif self.object.cust_26_act == 'C':
            table_data.append(0.17*0.5)
        elif self.object.cust_26_act == 'B':
            table_data.append(0.17*0.3)
        else: # A o nulo
            table_data.append(0.0)

        if self.object.cust_26_p1 == 'E': 
            table_data.append(0.17*1.0)
        elif self.object.cust_26_p1 == 'D':
            table_data.append(0.17*0.7)
        elif self.object.cust_26_p1 == 'C':
            table_data.append(0.17*0.5)
        elif self.object.cust_26_p1 == 'B':
            table_data.append(0.17*0.3)
        else: # A o nulo
            table_data.append(0.0)
  
        if self.object.cust_26_p2 == 'E': 
            table_data.append(0.17*1.0)
        elif self.object.cust_26_p2 == 'D':
            table_data.append(0.17*0.7)
        elif self.object.cust_26_p2 == 'C':
            table_data.append(0.17*0.5)
        elif self.object.cust_26_p2 == 'B':
            table_data.append(0.17*0.3)
        else: # A o nulo
            table_data.append(0.0)
        #cust 3.1
        if self.object.cust_31_act == 'D': 
            table_data.append(0.1*1.0)
        elif self.object.cust_31_act == 'C':
            table_data.append(0.1*0.7)
        elif self.object.cust_31_act == 'B':
            table_data.append(0.1*0.3)
        else: # A o nulo
            table_data.append(0.0)

        if self.object.cust_31_p1 == 'D': 
            table_data.append(0.1*1.0)
        elif self.object.cust_31_p1 == 'C':
            table_data.append(0.1*0.7)
        elif self.object.cust_31_p1 == 'B':
            table_data.append(0.1*0.3)
        else: # A o nulo
            table_data.append(0.0)
  
        if self.object.cust_31_p2 == 'D': 
            table_data.append(0.1*1.0)
        elif self.object.cust_31_p2 == 'C':
            table_data.append(0.1*0.7)
        elif self.object.cust_31_p2 == 'B':
            table_data.append(0.1*0.3)
        else: # A o nulo
            table_data.append(0.0)
       #cust 3.2
        if self.object.cust_32_act == 'E': 
            table_data.append(0.12*1.0)
        elif self.object.cust_32_act == 'D':
            table_data.append(0.12*0.7)
        elif self.object.cust_32_act == 'C':
            table_data.append(0.12*0.5)
        elif self.object.cust_32_act == 'B':
            table_data.append(0.12*0.3)
        else: # A o nulo
            table_data.append(0.0)

        if self.object.cust_32_p1 == 'E': 
            table_data.append(0.12*1.0)
        elif self.object.cust_32_p1 == 'D':
            table_data.append(0.12*0.7)
        elif self.object.cust_32_p1 == 'C':
            table_data.append(0.12*0.5)
        elif self.object.cust_32_p1 == 'B':
            table_data.append(0.12*0.3)
        else: # A o nulo
            table_data.append(0.0)
  
        if self.object.cust_32_p2 == 'E': 
            table_data.append(0.12*1.0)
        elif self.object.cust_32_p2 == 'D':
            table_data.append(0.12*0.7)
        elif self.object.cust_32_p2 == 'C':
            table_data.append(0.12*0.5)
        elif self.object.cust_32_p2 == 'B':
            table_data.append(0.12*0.3)
        else: # A o nulo
            table_data.append(0.0)
       #cust 3.3
        if self.object.cust_33_act == 'E': 
            table_data.append(0.1*1.0)
        elif self.object.cust_33_act == 'D':
            table_data.append(0.1*0.7)
        elif self.object.cust_33_act == 'C':
            table_data.append(0.1*0.5)
        elif self.object.cust_33_act == 'B':
            table_data.append(0.1*0.3)
        else: # A o nulo
            table_data.append(0.0)

        if self.object.cust_33_p1 == 'E': 
            table_data.append(0.1*1.0)
        elif self.object.cust_33_p1 == 'D':
            table_data.append(0.1*0.7)
        elif self.object.cust_33_p1 == 'C':
            table_data.append(0.1*0.5)
        elif self.object.cust_33_p1 == 'B':
            table_data.append(0.1*0.3)
        else: # A o nulo
            table_data.append(0.0)
  
        if self.object.cust_33_p2 == 'E': 
            table_data.append(0.1*1.0)
        elif self.object.cust_33_p2 == 'D':
            table_data.append(0.1*0.7)
        elif self.object.cust_33_p2 == 'C':
            table_data.append(0.1*0.5)
        elif self.object.cust_33_p2 == 'B':
            table_data.append(0.1*0.3)
        else: # A o nulo
            table_data.append(0.0)
       #cust 3.4
        if self.object.cust_34_act == 'E': 
            table_data.append(0.12*1.0)
        elif self.object.cust_34_act == 'D':
            table_data.append(0.12*0.7)
        elif self.object.cust_34_act == 'C':
            table_data.append(0.12*0.5)
        elif self.object.cust_34_act == 'B':
            table_data.append(0.12*0.3)
        else: # A o nulo
            table_data.append(0.0)

        if self.object.cust_34_p1 == 'E': 
            table_data.append(0.12*1.0)
        elif self.object.cust_34_p1 == 'D':
            table_data.append(0.12*0.7)
        elif self.object.cust_34_p1 == 'C':
            table_data.append(0.12*0.5)
        elif self.object.cust_34_p1 == 'B':
            table_data.append(0.12*0.3)
        else: # A o nulo
            table_data.append(0.0)
  
        if self.object.cust_34_p2 == 'E': 
            table_data.append(0.12*1.0)
        elif self.object.cust_34_p2 == 'D':
            table_data.append(0.12*0.7)
        elif self.object.cust_34_p2 == 'C':
            table_data.append(0.12*0.5)
        elif self.object.cust_34_p2 == 'B':
            table_data.append(0.12*0.3)
        else: # A o nulo
            table_data.append(0.0)
       #cust 3.5
        if self.object.cust_35_act == 'E': 
            table_data.append(0.12*1.0)
        elif self.object.cust_35_act == 'D':
            table_data.append(0.12*0.7)
        elif self.object.cust_35_act == 'C':
            table_data.append(0.12*0.5)
        elif self.object.cust_35_act == 'B':
            table_data.append(0.12*0.3)
        else: # A o nulo
            table_data.append(0.0)

        if self.object.cust_35_p1 == 'E': 
            table_data.append(0.12*1.0)
        elif self.object.cust_35_p1 == 'D':
            table_data.append(0.12*0.7)
        elif self.object.cust_35_p1 == 'C':
            table_data.append(0.12*0.5)
        elif self.object.cust_35_p1 == 'B':
            table_data.append(0.12*0.3)
        else: # A o nulo
            table_data.append(0.0)
  
        if self.object.cust_35_p2 == 'E': 
            table_data.append(0.12*1.0)
        elif self.object.cust_35_p2 == 'D':
            table_data.append(0.12*0.7)
        elif self.object.cust_35_p2 == 'C':
            table_data.append(0.12*0.5)
        elif self.object.cust_35_p2 == 'B':
            table_data.append(0.12*0.3)
        else: # A o nulo
            table_data.append(0.0)
      #cust 3.6
        if self.object.cust_36_act == 'E': 
            table_data.append(0.12*1.0)
        elif self.object.cust_36_act == 'D':
            table_data.append(0.12*0.7)
        elif self.object.cust_36_act == 'C':
            table_data.append(0.12*0.5)
        elif self.object.cust_36_act == 'B':
            table_data.append(0.12*0.3)
        else: # A o nulo
            table_data.append(0.0)

        if self.object.cust_36_p1 == 'E': 
            table_data.append(0.12*1.0)
        elif self.object.cust_36_p1 == 'D':
            table_data.append(0.12*0.7)
        elif self.object.cust_36_p1 == 'C':
            table_data.append(0.12*0.5)
        elif self.object.cust_36_p1 == 'B':
            table_data.append(0.12*0.3)
        else: # A o nulo
            table_data.append(0.0)
  
        if self.object.cust_36_p2 == 'E': 
            table_data.append(0.12*1.0)
        elif self.object.cust_36_p2 == 'D':
            table_data.append(0.12*0.7)
        elif self.object.cust_36_p2 == 'C':
            table_data.append(0.12*0.5)
        elif self.object.cust_36_p2 == 'B':
            table_data.append(0.12*0.3)
        else: # A o nulo
            table_data.append(0.0)
       #cust 3.7
        if self.object.cust_37_act == 'E': 
            table_data.append(0.1*1.0)
        elif self.object.cust_37_act == 'D':
            table_data.append(0.1*0.7)
        elif self.object.cust_37_act == 'C':
            table_data.append(0.1*0.5)
        elif self.object.cust_37_act == 'B':
            table_data.append(0.1*0.3)
        else: # A o nulo
            table_data.append(0.0)

        if self.object.cust_37_p1 == 'E': 
            table_data.append(0.1*1.0)
        elif self.object.cust_37_p1 == 'D':
            table_data.append(0.1*0.7)
        elif self.object.cust_37_p1 == 'C':
            table_data.append(0.1*0.5)
        elif self.object.cust_37_p1 == 'B':
            table_data.append(0.1*0.3)
        else: # A o nulo
            table_data.append(0.0)
  
        if self.object.cust_37_p2 == 'E': 
            table_data.append(0.1*1.0)
        elif self.object.cust_37_p2 == 'D':
            table_data.append(0.1*0.7)
        elif self.object.cust_37_p2 == 'C':
            table_data.append(0.1*0.5)
        elif self.object.cust_37_p2 == 'B':
            table_data.append(0.1*0.3)
        else: # A o nulo
            table_data.append(0.0)
        #cust 3.8
        if self.object.cust_38_act == 'D': 
            table_data.append(0.12*1.0)
        elif self.object.cust_38_act == 'C':
            table_data.append(0.12*0.7)
        elif self.object.cust_38_act == 'B':
            table_data.append(0.12*0.5)
        else: # A o nulo
            table_data.append(0.0)

        if self.object.cust_38_p1 == 'D': 
            table_data.append(0.12*1.0)
        elif self.object.cust_38_p1 == 'C':
            table_data.append(0.12*0.7)
        elif self.object.cust_38_p1 == 'B':
            table_data.append(0.12*0.5)
        else: # A o nulo
            table_data.append(0.0)
  
        if self.object.cust_38_p2 == 'D': 
            table_data.append(0.12*1.0)
        elif self.object.cust_38_p2 == 'C':
            table_data.append(0.12*0.7)
        elif self.object.cust_38_p2 == 'B':
            table_data.append(0.12*0.5)
        else: # A o nulo
            table_data.append(0.0)
       #cust 3.9
        if self.object.cust_39_act == 'E': 
            table_data.append(0.1*1.0)
        elif self.object.cust_39_act == 'D':
            table_data.append(0.1*0.7)
        elif self.object.cust_39_act == 'C':
            table_data.append(0.1*0.5)
        elif self.object.cust_39_act == 'B':
            table_data.append(0.1*0.3)
        else: # A o nulo
            table_data.append(0.0)

        if self.object.cust_39_p1 == 'E': 
            table_data.append(0.1*1.0)
        elif self.object.cust_39_p1 == 'D':
            table_data.append(0.1*0.7)
        elif self.object.cust_39_p1 == 'C':
            table_data.append(0.1*0.5)
        elif self.object.cust_39_p1 == 'B':
            table_data.append(0.1*0.3)
        else: # A o nulo
            table_data.append(0.0)
  
        if self.object.cust_39_p2 == 'E': 
            table_data.append(0.1*1.0)
        elif self.object.cust_39_p2 == 'D':
            table_data.append(0.1*0.7)
        elif self.object.cust_39_p2 == 'C':
            table_data.append(0.1*0.5)
        elif self.object.cust_39_p2 == 'B':
            table_data.append(0.1*0.3)
        else: # A o nulo
            table_data.append(0.0)
        #cust 4.1
        if self.object.cust_41_act == 'D': 
            table_data.append(0.15*1.0)
        elif self.object.cust_41_act == 'C':
            table_data.append(0.15*0.7)
        elif self.object.cust_41_act == 'B':
            table_data.append(0.15*0.5)
        else: # A o nulo
            table_data.append(0.0)

        if self.object.cust_41_p1 == 'D': 
            table_data.append(0.15*1.0)
        elif self.object.cust_41_p1 == 'C':
            table_data.append(0.15*0.7)
        elif self.object.cust_41_p1 == 'B':
            table_data.append(0.15*0.5)
        else: # A o nulo
            table_data.append(0.0)
  
        if self.object.cust_41_p2 == 'D': 
            table_data.append(0.15*1.0)
        elif self.object.cust_41_p2 == 'C':
            table_data.append(0.15*0.7)
        elif self.object.cust_41_p2 == 'B':
            table_data.append(0.15*0.5)
        else: # A o nulo
            table_data.append(0.0)
       #cust 4.2
        if self.object.cust_42_act == 'E': 
            table_data.append(0.13*1.0)
        elif self.object.cust_42_act == 'D':
            table_data.append(0.13*0.7)
        elif self.object.cust_42_act == 'C':
            table_data.append(0.13*0.5)
        elif self.object.cust_42_act == 'B':
            table_data.append(0.13*0.3)
        else: # A o nulo
            table_data.append(0.0)

        if self.object.cust_42_p1 == 'E': 
            table_data.append(0.13*1.0)
        elif self.object.cust_42_p1 == 'D':
            table_data.append(0.13*0.7)
        elif self.object.cust_42_p1 == 'C':
            table_data.append(0.13*0.5)
        elif self.object.cust_42_p1 == 'B':
            table_data.append(0.13*0.3)
        else: # A o nulo
            table_data.append(0.0)
  
        if self.object.cust_42_p2 == 'E': 
            table_data.append(0.13*1.0)
        elif self.object.cust_42_p2 == 'D':
            table_data.append(0.13*0.7)
        elif self.object.cust_42_p2 == 'C':
            table_data.append(0.13*0.5)
        elif self.object.cust_42_p2 == 'B':
            table_data.append(0.13*0.3)
        else: # A o nulo
            table_data.append(0.0)
       #cust 4.3
        if self.object.cust_43_act == 'E': 
            table_data.append(0.15*1.0)
        elif self.object.cust_43_act == 'D':
            table_data.append(0.15*0.7)
        elif self.object.cust_43_act == 'C':
            table_data.append(0.15*0.5)
        elif self.object.cust_43_act == 'B':
            table_data.append(0.15*0.3)
        else: # A o nulo
            table_data.append(0.0)

        if self.object.cust_43_p1 == 'E': 
            table_data.append(0.15*1.0)
        elif self.object.cust_43_p1 == 'D':
            table_data.append(0.15*0.7)
        elif self.object.cust_43_p1 == 'C':
            table_data.append(0.15*0.5)
        elif self.object.cust_43_p1 == 'B':
            table_data.append(0.15*0.3)
        else: # A o nulo
            table_data.append(0.0)
  
        if self.object.cust_43_p2 == 'E': 
            table_data.append(0.15*1.0)
        elif self.object.cust_43_p2 == 'D':
            table_data.append(0.15*0.7)
        elif self.object.cust_43_p2 == 'C':
            table_data.append(0.15*0.5)
        elif self.object.cust_43_p2 == 'B':
            table_data.append(0.15*0.3)
        else: # A o nulo
            table_data.append(0.0)
       #cust 4.4
        if self.object.cust_44_act == 'E': 
            table_data.append(0.15*1.0)
        elif self.object.cust_44_act == 'D':
            table_data.append(0.15*0.7)
        elif self.object.cust_44_act == 'C':
            table_data.append(0.15*0.5)
        elif self.object.cust_44_act == 'B':
            table_data.append(0.15*0.3)
        else: # A o nulo
            table_data.append(0.0)

        if self.object.cust_44_p1 == 'E': 
            table_data.append(0.15*1.0)
        elif self.object.cust_44_p1 == 'D':
            table_data.append(0.15*0.7)
        elif self.object.cust_44_p1 == 'C':
            table_data.append(0.15*0.5)
        elif self.object.cust_44_p1 == 'B':
            table_data.append(0.15*0.3)
        else: # A o nulo
            table_data.append(0.0)
  
        if self.object.cust_44_p2 == 'E': 
            table_data.append(0.15*1.0)
        elif self.object.cust_44_p2 == 'D':
            table_data.append(0.15*0.7)
        elif self.object.cust_44_p2 == 'C':
            table_data.append(0.15*0.5)
        elif self.object.cust_44_p2 == 'B':
            table_data.append(0.15*0.3)
        else: # A o nulo
            table_data.append(0.0)
       #cust 4.5
        if self.object.cust_45_act == 'E': 
            table_data.append(0.15*1.0)
        elif self.object.cust_45_act == 'D':
            table_data.append(0.15*0.7)
        elif self.object.cust_45_act == 'C':
            table_data.append(0.15*0.5)
        elif self.object.cust_45_act == 'B':
            table_data.append(0.15*0.3)
        else: # A o nulo
            table_data.append(0.0)

        if self.object.cust_45_p1 == 'E': 
            table_data.append(0.15*1.0)
        elif self.object.cust_45_p1 == 'D':
            table_data.append(0.15*0.7)
        elif self.object.cust_45_p1 == 'C':
            table_data.append(0.15*0.5)
        elif self.object.cust_45_p1 == 'B':
            table_data.append(0.15*0.3)
        else: # A o nulo
            table_data.append(0.0)
  
        if self.object.cust_45_p2 == 'E': 
            table_data.append(0.15*1.0)
        elif self.object.cust_45_p2 == 'D':
            table_data.append(0.15*0.7)
        elif self.object.cust_45_p2 == 'C':
            table_data.append(0.15*0.5)
        elif self.object.cust_45_p2 == 'B':
            table_data.append(0.15*0.3)
        else: # A o nulo
            table_data.append(0.0)
       #cust 4.6
        if self.object.cust_46_act == 'E': 
            table_data.append(0.15*1.0)
        elif self.object.cust_46_act == 'D':
            table_data.append(0.15*0.7)
        elif self.object.cust_46_act == 'C':
            table_data.append(0.15*0.5)
        elif self.object.cust_46_act == 'B':
            table_data.append(0.15*0.3)
        else: # A o nulo
            table_data.append(0.0)

        if self.object.cust_46_p1 == 'E': 
            table_data.append(0.15*1.0)
        elif self.object.cust_46_p1 == 'D':
            table_data.append(0.15*0.7)
        elif self.object.cust_46_p1 == 'C':
            table_data.append(0.15*0.5)
        elif self.object.cust_46_p1 == 'B':
            table_data.append(0.15*0.3)
        else: # A o nulo
            table_data.append(0.0)
  
        if self.object.cust_46_p2 == 'E': 
            table_data.append(0.15*1.0)
        elif self.object.cust_46_p2 == 'D':
            table_data.append(0.15*0.7)
        elif self.object.cust_46_p2 == 'C':
            table_data.append(0.15*0.5)
        elif self.object.cust_46_p2 == 'B':
            table_data.append(0.15*0.3)
        else: # A o nulo
            table_data.append(0.0)
       #cust 4.7
        if self.object.cust_47_act == 'E': 
            table_data.append(0.12*1.0)
        elif self.object.cust_47_act == 'D':
            table_data.append(0.12*0.7)
        elif self.object.cust_47_act == 'C':
            table_data.append(0.12*0.5)
        elif self.object.cust_47_act == 'B':
            table_data.append(0.12*0.3)
        else: # A o nulo
            table_data.append(0.0)

        if self.object.cust_47_p1 == 'E': 
            table_data.append(0.12*1.0)
        elif self.object.cust_47_p1 == 'D':
            table_data.append(0.12*0.7)
        elif self.object.cust_47_p1 == 'C':
            table_data.append(0.12*0.5)
        elif self.object.cust_47_p1 == 'B':
            table_data.append(0.12*0.3)
        else: # A o nulo
            table_data.append(0.0)
  
        if self.object.cust_47_p2 == 'E': 
            table_data.append(0.12*1.0)
        elif self.object.cust_47_p2 == 'D':
            table_data.append(0.12*0.7)
        elif self.object.cust_47_p2 == 'C':
            table_data.append(0.12*0.5)
        elif self.object.cust_47_p2 == 'B':
            table_data.append(0.12*0.3)
        else: # A o nulo
            table_data.append(0.0)
       #cust 5.1
        if self.object.cust_51_act == 'E': 
            table_data.append(0.22*1.0)
        elif self.object.cust_51_act == 'D':
            table_data.append(0.22*0.7)
        elif self.object.cust_51_act == 'C':
            table_data.append(0.22*0.5)
        elif self.object.cust_51_act == 'B':
            table_data.append(0.22*0.3)
        else: # A o nulo
            table_data.append(0.0)

        if self.object.cust_51_p1 == 'E': 
            table_data.append(0.22*1.0)
        elif self.object.cust_51_p1 == 'D':
            table_data.append(0.22*0.7)
        elif self.object.cust_51_p1 == 'C':
            table_data.append(0.22*0.5)
        elif self.object.cust_51_p1 == 'B':
            table_data.append(0.22*0.3)
        else: # A o nulo
            table_data.append(0.0)
  
        if self.object.cust_51_p2 == 'E': 
            table_data.append(0.22*1.0)
        elif self.object.cust_51_p2 == 'D':
            table_data.append(0.22*0.7)
        elif self.object.cust_51_p2 == 'C':
            table_data.append(0.22*0.5)
        elif self.object.cust_51_p2 == 'B':
            table_data.append(0.22*0.3)
        else: # A o nulo
            table_data.append(0.0)
       #cust 5.2
        if self.object.cust_52_act == 'E': 
            table_data.append(0.22*1.0)
        elif self.object.cust_52_act == 'D':
            table_data.append(0.22*0.7)
        elif self.object.cust_52_act == 'C':
            table_data.append(0.22*0.5)
        elif self.object.cust_52_act == 'B':
            table_data.append(0.22*0.3)
        else: # A o nulo
            table_data.append(0.0)

        if self.object.cust_52_p1 == 'E': 
            table_data.append(0.22*1.0)
        elif self.object.cust_52_p1 == 'D':
            table_data.append(0.22*0.7)
        elif self.object.cust_52_p1 == 'C':
            table_data.append(0.22*0.5)
        elif self.object.cust_52_p1 == 'B':
            table_data.append(0.22*0.3)
        else: # A o nulo
            table_data.append(0.0)
  
        if self.object.cust_52_p2 == 'E': 
            table_data.append(0.22*1.0)
        elif self.object.cust_52_p2 == 'D':
            table_data.append(0.22*0.7)
        elif self.object.cust_52_p2 == 'C':
            table_data.append(0.22*0.5)
        elif self.object.cust_52_p2 == 'B':
            table_data.append(0.22*0.3)
        else: # A o nulo
            table_data.append(0.0)
       #cust 5.3
        if self.object.cust_53_act == 'E': 
            table_data.append(0.22*1.0)
        elif self.object.cust_53_act == 'D':
            table_data.append(0.22*0.7)
        elif self.object.cust_53_act == 'C':
            table_data.append(0.22*0.5)
        elif self.object.cust_53_act == 'B':
            table_data.append(0.22*0.3)
        else: # A o nulo
            table_data.append(0.0)

        if self.object.cust_53_p1 == 'E': 
            table_data.append(0.22*1.0)
        elif self.object.cust_53_p1 == 'D':
            table_data.append(0.22*0.7)
        elif self.object.cust_53_p1 == 'C':
            table_data.append(0.22*0.5)
        elif self.object.cust_53_p1 == 'B':
            table_data.append(0.22*0.3)
        else: # A o nulo
            table_data.append(0.0)
  
        if self.object.cust_53_p2 == 'E': 
            table_data.append(0.22*1.0)
        elif self.object.cust_53_p2 == 'D':
            table_data.append(0.22*0.7)
        elif self.object.cust_53_p2 == 'C':
            table_data.append(0.22*0.5)
        elif self.object.cust_53_p2 == 'B':
            table_data.append(0.22*0.3)
        else: # A o nulo
            table_data.append(0.0)
        #cust 5.4
        if self.object.cust_54_act == 'D': 
            table_data.append(0.15*1.0)
        elif self.object.cust_54_act == 'C':
            table_data.append(0.15*0.7)
        elif self.object.cust_54_act == 'B':
            table_data.append(0.15*0.3)
        else: # A o nulo
            table_data.append(0.0)

        if self.object.cust_54_p1 == 'D': 
            table_data.append(0.15*1.0)
        elif self.object.cust_54_p1 == 'C':
            table_data.append(0.15*0.7)
        elif self.object.cust_54_p1 == 'B':
            table_data.append(0.15*0.3)
        else: # A o nulo
            table_data.append(0.0)
  
        if self.object.cust_54_p2 == 'D': 
            table_data.append(0.15*1.0)
        elif self.object.cust_54_p2 == 'C':
            table_data.append(0.15*0.7)
        elif self.object.cust_54_p2 == 'B':
            table_data.append(0.15*0.3)
        else: # A o nulo
            table_data.append(0.0)
        #cust 5.5
        if self.object.cust_55_act == 'D': 
            table_data.append(0.19*1.0)
        elif self.object.cust_55_act == 'C':
            table_data.append(0.19*0.5)
        elif self.object.cust_55_act == 'B':
            table_data.append(0.19*0.5)
        else: # A o nulo
            table_data.append(0.0)

        if self.object.cust_55_p1 == 'D': 
            table_data.append(0.19*1.0)
        elif self.object.cust_55_p1 == 'C':
            table_data.append(0.19*0.5)
        elif self.object.cust_55_p1 == 'B':
            table_data.append(0.19*0.5)
        else: # A o nulo
            table_data.append(0.0)
  
        if self.object.cust_55_p2 == 'D': 
            table_data.append(0.19*1.0)
        elif self.object.cust_55_p2 == 'C':
            table_data.append(0.19*0.5)
        elif self.object.cust_55_p2 == 'B':
            table_data.append(0.19*0.5)
        else: # A o nulo
            table_data.append(0.0)

        return table_data
    
    def get_table_data_vci(self):
        table_data = [] #lista vacia para almacenar resultados 
        #############VCI#################
       #vci 1.1
        if self.object.vci_11_act == 'D': 
            table_data.append(0.15*1.0)
        elif self.object.vci_11_act == 'C':
            table_data.append(0.15*0.7)
        elif self.object.vci_11_act == 'B':
            table_data.append(0.15*0.5)
        else: # A o nulo
            table_data.append(0.0)

        if self.object.vci_11_p1 == 'D': 
            table_data.append(0.15*1.0)
        elif self.object.vci_11_p1 == 'C':
            table_data.append(0.15*0.7)
        elif self.object.vci_11_p1 == 'B':
            table_data.append(0.15*0.5)
        else: # A o nulo
            table_data.append(0.0)
  
        if self.object.vci_11_p2 == 'D': 
            table_data.append(0.15*1.0)
        elif self.object.vci_11_p2 == 'C':
            table_data.append(0.15*0.7)
        elif self.object.vci_11_p2 == 'B':
            table_data.append(0.15*0.5)
        else: # A o nulo
            table_data.append(0.0)
        #vci 1.2
        if self.object.vci_12_act == 'D': 
            table_data.append(0.2*1.0)
        elif self.object.vci_12_act == 'C':
            table_data.append(0.2*0.7)
        elif self.object.vci_12_act == 'B':
            table_data.append(0.2*0.5)
        else: # A o nulo
            table_data.append(0.0)

        if self.object.vci_12_p1 == 'D': 
            table_data.append(0.2*1.0)
        elif self.object.vci_12_p1 == 'C':
            table_data.append(0.2*0.7)
        elif self.object.vci_12_p1 == 'B':
            table_data.append(0.2*0.5)
        else: # A o nulo
            table_data.append(0.0)
  
        if self.object.vci_12_p2 == 'D': 
            table_data.append(0.2*1.0)
        elif self.object.vci_12_p2 == 'C':
            table_data.append(0.2*0.7)
        elif self.object.vci_12_p2 == 'B':
            table_data.append(0.2*0.5)
        else: # A o nulo
            table_data.append(0.0)
        #vci 1.3
        if self.object.vci_13_act == 'D': 
            table_data.append(0.2*1.0)
        elif self.object.vci_13_act == 'C':
            table_data.append(0.2*0.7)
        elif self.object.vci_13_act == 'B':
            table_data.append(0.2*0.5)
        else: # A o nulo
            table_data.append(0.0)

        if self.object.vci_13_p1 == 'D': 
            table_data.append(0.2*1.0)
        elif self.object.vci_13_p1 == 'C':
            table_data.append(0.2*0.7)
        elif self.object.vci_13_p1 == 'B':
            table_data.append(0.2*0.5)
        else: # A o nulo
            table_data.append(0.0)
  
        if self.object.vci_13_p2 == 'D': 
            table_data.append(0.2*1.0)
        elif self.object.vci_13_p2 == 'C':
            table_data.append(0.2*0.7)
        elif self.object.vci_13_p2 == 'B':
            table_data.append(0.2*0.5)
        else: # A o nulo
            table_data.append(0.0)
        #vci 1.4
        if self.object.vci_14_act == 'D': 
            table_data.append(0.3*1.0)
        elif self.object.vci_14_act == 'C':
            table_data.append(0.3*0.7)
        elif self.object.vci_14_act == 'B':
            table_data.append(0.3*0.3)
        else: # A o nulo
            table_data.append(0.0)

        if self.object.vci_14_p1 == 'D': 
            table_data.append(0.3*1.0)
        elif self.object.vci_14_p1 == 'C':
            table_data.append(0.3*0.7)
        elif self.object.vci_14_p1 == 'B':
            table_data.append(0.3*0.3)
        else: # A o nulo
            table_data.append(0.0)
  
        if self.object.vci_14_p2 == 'D': 
            table_data.append(0.3*1.0)
        elif self.object.vci_14_p2 == 'C':
            table_data.append(0.3*0.7)
        elif self.object.vci_14_p2 == 'B':
            table_data.append(0.3*0.3)
        else: # A o nulo
            table_data.append(0.0)
        #vci 1.5
        if self.object.vci_15_act == 'D': 
            table_data.append(0.15*1.0)
        elif self.object.vci_15_act == 'C':
            table_data.append(0.15*0.7)
        elif self.object.vci_15_act == 'B':
            table_data.append(0.15*0.5)
        else: # A o nulo
            table_data.append(0.0)

        if self.object.vci_15_p1 == 'D': 
            table_data.append(0.15*1.0)
        elif self.object.vci_15_p1 == 'C':
            table_data.append(0.15*0.7)
        elif self.object.vci_15_p1 == 'B':
            table_data.append(0.15*0.5)
        else: # A o nulo
            table_data.append(0.0)
  
        if self.object.vci_15_p2 == 'D': 
            table_data.append(0.15*1.0)
        elif self.object.vci_15_p2 == 'C':
            table_data.append(0.15*0.7)
        elif self.object.vci_15_p2 == 'B':
            table_data.append(0.15*0.5)
        else: # A o nulo
            table_data.append(0.0)
       #vci 2.1
        if self.object.vci_21_act == 'E': 
            table_data.append(0.25*1.0)
        elif self.object.vci_21_act == 'D':
            table_data.append(0.25*0.7)
        elif self.object.vci_21_act == 'C':
            table_data.append(0.25*0.5)
        elif self.object.vci_21_act == 'B':
            table_data.append(0.25*0.3)
        else: # A o nulo
            table_data.append(0.0)

        if self.object.vci_21_p1 == 'E': 
            table_data.append(0.25*1.0)
        elif self.object.vci_21_p1 == 'D':
            table_data.append(0.25*0.7)
        elif self.object.vci_21_p1 == 'C':
            table_data.append(0.25*0.5)
        elif self.object.vci_21_p1 == 'B':
            table_data.append(0.25*0.3)
        else: # A o nulo
            table_data.append(0.0)
  
        if self.object.vci_21_p2 == 'E': 
            table_data.append(0.25*1.0)
        elif self.object.vci_21_p2 == 'D':
            table_data.append(0.25*0.7)
        elif self.object.vci_21_p2 == 'C':
            table_data.append(0.25*0.5)
        elif self.object.vci_21_p2 == 'B':
            table_data.append(0.25*0.3)
        else: # A o nulo
            table_data.append(0.0)
        #vci 2.2
        if self.object.vci_22_act == 'D': 
            table_data.append(0.25*1.0)
        elif self.object.vci_22_act == 'C':
            table_data.append(0.25*0.5)
        elif self.object.vci_22_act == 'B':
            table_data.append(0.25*0.3)
        else: # A o nulo
            table_data.append(0.0)

        if self.object.vci_22_p1 == 'D': 
            table_data.append(0.25*1.0)
        elif self.object.vci_22_p1 == 'C':
            table_data.append(0.25*0.5)
        elif self.object.vci_22_p1 == 'B':
            table_data.append(0.25*0.3)
        else: # A o nulo
            table_data.append(0.0)
  
        if self.object.vci_22_p2 == 'D': 
            table_data.append(0.25*1.0)
        elif self.object.vci_22_p2 == 'C':
            table_data.append(0.25*0.5)
        elif self.object.vci_22_p2 == 'B':
            table_data.append(0.25*0.3)
        else: # A o nulo
            table_data.append(0.0)
       #vci 2.3
        if self.object.vci_23_act == 'E': 
            table_data.append(0.3*1.0)
        elif self.object.vci_23_act == 'D':
            table_data.append(0.3*0.7)
        elif self.object.vci_23_act == 'C':
            table_data.append(0.3*0.5)
        elif self.object.vci_23_act == 'B':
            table_data.append(0.3*0.3)
        else: # A o nulo
            table_data.append(0.0)

        if self.object.vci_23_p1 == 'E': 
            table_data.append(0.3*1.0)
        elif self.object.vci_23_p1 == 'D':
            table_data.append(0.3*0.7)
        elif self.object.vci_23_p1 == 'C':
            table_data.append(0.3*0.5)
        elif self.object.vci_23_p1 == 'B':
            table_data.append(0.3*0.3)
        else: # A o nulo
            table_data.append(0.0)
  
        if self.object.vci_23_p2 == 'E': 
            table_data.append(0.3*1.0)
        elif self.object.vci_23_p2 == 'D':
            table_data.append(0.3*0.7)
        elif self.object.vci_23_p2 == 'C':
            table_data.append(0.3*0.5)
        elif self.object.vci_23_p2 == 'B':
            table_data.append(0.3*0.3)
        else: # A o nulo
            table_data.append(0.0)
       #vci 2.4
        if self.object.vci_24_act == 'E': 
            table_data.append(0.2*1.0)
        elif self.object.vci_24_act == 'D':
            table_data.append(0.2*0.7)
        elif self.object.vci_24_act == 'C':
            table_data.append(0.2*0.5)
        elif self.object.vci_24_act == 'B':
            table_data.append(0.2*0.3)
        else: # A o nulo
            table_data.append(0.0)

        if self.object.vci_24_p1 == 'E': 
            table_data.append(0.2*1.0)
        elif self.object.vci_24_p1 == 'D':
            table_data.append(0.2*0.7)
        elif self.object.vci_24_p1 == 'C':
            table_data.append(0.2*0.5)
        elif self.object.vci_24_p1 == 'B':
            table_data.append(0.2*0.3)
        else: # A o nulo
            table_data.append(0.0)
  
        if self.object.vci_24_p2 == 'E': 
            table_data.append(0.2*1.0)
        elif self.object.vci_24_p2 == 'D':
            table_data.append(0.2*0.7)
        elif self.object.vci_24_p2 == 'C':
            table_data.append(0.2*0.5)
        elif self.object.vci_24_p2 == 'B':
            table_data.append(0.2*0.3)
        else: # A o nulo
            table_data.append(0.0)
       #vci 3.1
        if self.object.vci_31_act == 'E': 
            table_data.append(0.3*1.0)
        elif self.object.vci_31_act == 'D':
            table_data.append(0.3*0.7)
        elif self.object.vci_31_act == 'C':
            table_data.append(0.3*0.5)
        elif self.object.vci_31_act == 'B':
            table_data.append(0.3*0.3)
        else: # A o nulo
            table_data.append(0.0)

        if self.object.vci_31_p1 == 'E': 
            table_data.append(0.3*1.0)
        elif self.object.vci_31_p1 == 'D':
            table_data.append(0.3*0.7)
        elif self.object.vci_31_p1 == 'C':
            table_data.append(0.3*0.5)
        elif self.object.vci_31_p1 == 'B':
            table_data.append(0.3*0.3)
        else: # A o nulo
            table_data.append(0.0)
  
        if self.object.vci_31_p2 == 'E': 
            table_data.append(0.3*1.0)
        elif self.object.vci_31_p2 == 'D':
            table_data.append(0.3*0.7)
        elif self.object.vci_31_p2 == 'C':
            table_data.append(0.3*0.5)
        elif self.object.vci_31_p2 == 'B':
            table_data.append(0.3*0.3)
        else: # A o nulo
            table_data.append(0.0)
       #vci 3.2
        if self.object.vci_32_act == 'E': 
            table_data.append(0.25*1.0)
        elif self.object.vci_32_act == 'D':
            table_data.append(0.25*0.7)
        elif self.object.vci_32_act == 'C':
            table_data.append(0.25*0.5)
        elif self.object.vci_32_act == 'B':
            table_data.append(0.25*0.3)
        else: # A o nulo
            table_data.append(0.0)

        if self.object.vci_32_p1 == 'E': 
            table_data.append(0.25*1.0)
        elif self.object.vci_32_p1 == 'D':
            table_data.append(0.25*0.7)
        elif self.object.vci_32_p1 == 'C':
            table_data.append(0.25*0.5)
        elif self.object.vci_32_p1 == 'B':
            table_data.append(0.25*0.3)
        else: # A o nulo
            table_data.append(0.0)
  
        if self.object.vci_32_p2 == 'E': 
            table_data.append(0.25*1.0)
        elif self.object.vci_32_p2 == 'D':
            table_data.append(0.25*0.7)
        elif self.object.vci_32_p2 == 'C':
            table_data.append(0.25*0.5)
        elif self.object.vci_32_p2 == 'B':
            table_data.append(0.25*0.3)
        else: # A o nulo
            table_data.append(0.0)
       #vci 3.3
        if self.object.vci_33_act == 'E': 
            table_data.append(0.3*1.0)
        elif self.object.vci_33_act == 'D':
            table_data.append(0.3*0.7)
        elif self.object.vci_33_act == 'C':
            table_data.append(0.3*0.5)
        elif self.object.vci_33_act == 'B':
            table_data.append(0.3*0.3)
        else: # A o nulo
            table_data.append(0.0)

        if self.object.vci_33_p1 == 'E': 
            table_data.append(0.3*1.0)
        elif self.object.vci_33_p1 == 'D':
            table_data.append(0.3*0.7)
        elif self.object.vci_33_p1 == 'C':
            table_data.append(0.3*0.5)
        elif self.object.vci_33_p1 == 'B':
            table_data.append(0.3*0.3)
        else: # A o nulo
            table_data.append(0.0)
  
        if self.object.vci_33_p2 == 'E': 
            table_data.append(0.3*1.0)
        elif self.object.vci_33_p2 == 'D':
            table_data.append(0.3*0.7)
        elif self.object.vci_33_p2 == 'C':
            table_data.append(0.3*0.5)
        elif self.object.vci_33_p2 == 'B':
            table_data.append(0.3*0.3)
        else: # A o nulo
            table_data.append(0.0)
       #vci 3.4
        if self.object.vci_34_act == 'E': 
            table_data.append(0.15*1.0)
        elif self.object.vci_34_act == 'D':
            table_data.append(0.15*0.7)
        elif self.object.vci_34_act == 'C':
            table_data.append(0.15*0.5)
        elif self.object.vci_34_act == 'B':
            table_data.append(0.15*0.3)
        else: # A o nulo
            table_data.append(0.0)

        if self.object.vci_34_p1 == 'E': 
            table_data.append(0.15*1.0)
        elif self.object.vci_34_p1 == 'D':
            table_data.append(0.15*0.7)
        elif self.object.vci_34_p1 == 'C':
            table_data.append(0.15*0.5)
        elif self.object.vci_34_p1 == 'B':
            table_data.append(0.15*0.3)
        else: # A o nulo
            table_data.append(0.0)
  
        if self.object.vci_34_p2 == 'E': 
            table_data.append(0.15*1.0)
        elif self.object.vci_34_p2 == 'D':
            table_data.append(0.15*0.7)
        elif self.object.vci_34_p2 == 'C':
            table_data.append(0.15*0.5)
        elif self.object.vci_34_p2 == 'B':
            table_data.append(0.15*0.3)
        else: # A o nulo
            table_data.append(0.0)
       #vci 4.1
        if self.object.vci_41_act == 'E': 
            table_data.append(0.25*1.0)
        elif self.object.vci_41_act == 'D':
            table_data.append(0.25*0.7)
        elif self.object.vci_41_act == 'C':
            table_data.append(0.25*0.5)
        elif self.object.vci_41_act == 'B':
            table_data.append(0.25*0.3)
        else: # A o nulo
            table_data.append(0.0)

        if self.object.vci_41_p1 == 'E': 
            table_data.append(0.25*1.0)
        elif self.object.vci_41_p1 == 'D':
            table_data.append(0.25*0.7)
        elif self.object.vci_41_p1 == 'C':
            table_data.append(0.25*0.5)
        elif self.object.vci_41_p1 == 'B':
            table_data.append(0.25*0.3)
        else: # A o nulo
            table_data.append(0.0)
  
        if self.object.vci_41_p2 == 'E': 
            table_data.append(0.25*1.0)
        elif self.object.vci_41_p2 == 'D':
            table_data.append(0.25*0.7)
        elif self.object.vci_41_p2 == 'C':
            table_data.append(0.25*0.5)
        elif self.object.vci_41_p2 == 'B':
            table_data.append(0.25*0.3)
        else: # A o nulo
            table_data.append(0.0)
       #vci 4.2
        if self.object.vci_42_act == 'E': 
            table_data.append(0.25*1.0)
        elif self.object.vci_42_act == 'D':
            table_data.append(0.25*0.7)
        elif self.object.vci_42_act == 'C':
            table_data.append(0.25*0.5)
        elif self.object.vci_42_act == 'B':
            table_data.append(0.25*0.3)
        else: # A o nulo
            table_data.append(0.0)

        if self.object.vci_42_p1 == 'E': 
            table_data.append(0.25*1.0)
        elif self.object.vci_42_p1 == 'D':
            table_data.append(0.25*0.7)
        elif self.object.vci_42_p1 == 'C':
            table_data.append(0.25*0.5)
        elif self.object.vci_42_p1 == 'B':
            table_data.append(0.25*0.3)
        else: # A o nulo
            table_data.append(0.0)
  
        if self.object.vci_42_p2 == 'E': 
            table_data.append(0.25*1.0)
        elif self.object.vci_42_p2 == 'D':
            table_data.append(0.25*0.7)
        elif self.object.vci_42_p2 == 'C':
            table_data.append(0.25*0.5)
        elif self.object.vci_42_p2 == 'B':
            table_data.append(0.25*0.3)
        else: # A o nulo
            table_data.append(0.0)
        #vci 4.3
        if self.object.vci_43_act == 'F': 
            table_data.append(0.25*1.0)
        elif self.object.vci_43_act == 'E':
            table_data.append(0.25*0.7)
        elif self.object.vci_43_act == 'D':
            table_data.append(0.25*0.5)
        elif self.object.vci_43_act == 'C':
            table_data.append(0.25*0.3)
        elif self.object.vci_43_act == 'B':
            table_data.append(0.25*0.3)
        else: # A o nulo
            table_data.append(0.0)

        if self.object.vci_43_p1 == 'F': 
            table_data.append(0.25*1.0)
        elif self.object.vci_43_p1 == 'E':
            table_data.append(0.25*0.7)
        elif self.object.vci_43_p1 == 'D':
            table_data.append(0.25*0.5)
        elif self.object.vci_43_p1 == 'C':
            table_data.append(0.25*0.3)
        elif self.object.vci_43_p1 == 'B':
            table_data.append(0.25*0.3)
        else: # A o nulo
            table_data.append(0.0)
  
        if self.object.vci_43_p2 == 'F': 
            table_data.append(0.25*1.0)
        elif self.object.vci_43_p2 == 'E':
            table_data.append(0.25*0.7)
        elif self.object.vci_43_p2 == 'D':
            table_data.append(0.25*0.5)
        elif self.object.vci_43_p2 == 'C':
            table_data.append(0.25*0.3)
        elif self.object.vci_43_p2 == 'B':
            table_data.append(0.25*0.3)
        else: # A o nulo
            table_data.append(0.0)
        #vci 4.4
        if self.object.vci_44_act == 'F': 
            table_data.append(0.25*1.0)
        elif self.object.vci_44_act == 'E':
            table_data.append(0.25*0.7)
        elif self.object.vci_44_act == 'D':
            table_data.append(0.25*0.5)
        elif self.object.vci_44_act == 'C':
            table_data.append(0.25*0.3)
        elif self.object.vci_44_act == 'B':
            table_data.append(0.25*0.3)
        else: # A o nulo
            table_data.append(0.0)

        if self.object.vci_44_p1 == 'F': 
            table_data.append(0.25*1.0)
        elif self.object.vci_44_p1 == 'E':
            table_data.append(0.25*0.7)
        elif self.object.vci_44_p1 == 'D':
            table_data.append(0.25*0.5)
        elif self.object.vci_44_p1 == 'C':
            table_data.append(0.25*0.3)
        elif self.object.vci_44_p1 == 'B':
            table_data.append(0.25*0.3)
        else: # A o nulo
            table_data.append(0.0)
  
        if self.object.vci_44_p2 == 'F': 
            table_data.append(0.25*1.0)
        elif self.object.vci_44_p2 == 'E':
            table_data.append(0.25*0.7)
        elif self.object.vci_44_p2 == 'D':
            table_data.append(0.25*0.5)
        elif self.object.vci_44_p2 == 'C':
            table_data.append(0.25*0.3)
        elif self.object.vci_44_p2 == 'B':
            table_data.append(0.25*0.3)
        else: # A o nulo
            table_data.append(0.0)
       #vci 5.1
        if self.object.vci_51_act == 'E': 
            table_data.append(0.33*1.0)
        elif self.object.vci_51_act == 'D':
            table_data.append(0.33*0.7)
        elif self.object.vci_51_act == 'C':
            table_data.append(0.33*0.5)
        elif self.object.vci_51_act == 'B':
            table_data.append(0.33*0.3)
        else: # A o nulo
            table_data.append(0.0)

        if self.object.vci_51_p1 == 'E': 
            table_data.append(0.33*1.0)
        elif self.object.vci_51_p1 == 'D':
            table_data.append(0.33*0.7)
        elif self.object.vci_51_p1 == 'C':
            table_data.append(0.33*0.5)
        elif self.object.vci_51_p1 == 'B':
            table_data.append(0.33*0.3)
        else: # A o nulo
            table_data.append(0.0)
  
        if self.object.vci_51_p2 == 'E': 
            table_data.append(0.33*1.0)
        elif self.object.vci_51_p2 == 'D':
            table_data.append(0.33*0.7)
        elif self.object.vci_51_p2 == 'C':
            table_data.append(0.33*0.5)
        elif self.object.vci_51_p2 == 'B':
            table_data.append(0.33*0.3)
        else: # A o nulo
            table_data.append(0.0)
        #vci 5.2
        if self.object.vci_52_act == 'F': 
            table_data.append(0.33*1.0)
        elif self.object.vci_52_act == 'E':
            table_data.append(0.33*0.7)
        elif self.object.vci_52_act == 'D':
            table_data.append(0.33*0.5)
        elif self.object.vci_52_act == 'C':
            table_data.append(0.33*0.3)
        elif self.object.vci_52_act == 'B':
            table_data.append(0.33*0.3)
        else: # A o nulo
            table_data.append(0.0)

        if self.object.vci_52_p1 == 'F': 
            table_data.append(0.33*1.0)
        elif self.object.vci_52_p1 == 'E':
            table_data.append(0.33*0.7)
        elif self.object.vci_52_p1 == 'D':
            table_data.append(0.33*0.5)
        elif self.object.vci_52_p1 == 'C':
            table_data.append(0.33*0.3)
        elif self.object.vci_52_p1 == 'B':
            table_data.append(0.33*0.3)
        else: # A o nulo
            table_data.append(0.0)
  
        if self.object.vci_52_p2 == 'F': 
            table_data.append(0.33*1.0)
        elif self.object.vci_52_p2 == 'E':
            table_data.append(0.33*0.7)
        elif self.object.vci_52_p2 == 'D':
            table_data.append(0.33*0.5)
        elif self.object.vci_52_p2 == 'C':
            table_data.append(0.33*0.3)
        elif self.object.vci_52_p2 == 'B':
            table_data.append(0.33*0.3)
        else: # A o nulo
            table_data.append(0.0)
        if self.object.vci_53_act == 'D': 
            table_data.append(0.34*1.0)
        elif self.object.vci_53_act == 'C':
            table_data.append(0.34*0.5)
        elif self.object.vci_53_act == 'B':
            table_data.append(0.34*0.3)
        else: # A o nulo
            table_data.append(0.0)

        if self.object.vci_53_p1 == 'D': 
            table_data.append(0.34*1.0)
        elif self.object.vci_53_p1 == 'C':
            table_data.append(0.34*0.5)
        elif self.object.vci_53_p1 == 'B':
            table_data.append(0.34*0.3)
        else: # A o nulo
            table_data.append(0.0)
  
        if self.object.vci_53_p2 == 'D': 
            table_data.append(0.34*1.0)
        elif self.object.vci_53_p2 == 'C':
            table_data.append(0.34*0.5)
        elif self.object.vci_53_p2 == 'B':
            table_data.append(0.34*0.3)
        else: # A o nulo
            table_data.append(0.0)

        return table_data

    def get_table_data_se(self):
        table_data = [] #lista vacia para almacenar resultados 
        #############SE#################
        #se 1.1
        if self.object.se_11_act == 'D': 
            table_data.append(0.4*1.0)
        elif self.object.se_11_act == 'C':
            table_data.append(0.4*0.7)
        elif self.object.se_11_act == 'B':
            table_data.append(0.4*0.5)
        else: # A o nulo
            table_data.append(0.0)

        if self.object.se_11_p1 == 'D': 
            table_data.append(0.4*1.0)
        elif self.object.se_11_p1 == 'C':
            table_data.append(0.4*0.7)
        elif self.object.se_11_p1 == 'B':
            table_data.append(0.4*0.5)
        else: # A o nulo
            table_data.append(0.0)
  
        if self.object.se_11_p2 == 'D': 
            table_data.append(0.4*1.0)
        elif self.object.se_11_p2 == 'C':
            table_data.append(0.4*0.7)
        elif self.object.se_11_p2 == 'B':
            table_data.append(0.4*0.5)
        else: # A o nulo
            table_data.append(0.0)
       #se 1.2
        if self.object.se_12_act == 'E': 
            table_data.append(0.25*1.0)
        elif self.object.se_12_act == 'D':
            table_data.append(0.25*0.8)
        elif self.object.se_12_act == 'C':
            table_data.append(0.25*0.65)
        elif self.object.se_12_act == 'B':
            table_data.append(0.25*0.5)
        else: # A o nulo
            table_data.append(0.0)

        if self.object.se_12_p1 == 'E': 
            table_data.append(0.25*1.0)
        elif self.object.se_12_p1 == 'D':
            table_data.append(0.25*0.8)
        elif self.object.se_12_p1 == 'C':
            table_data.append(0.25*0.65)
        elif self.object.se_12_p1 == 'B':
            table_data.append(0.25*0.5)
        else: # A o nulo
            table_data.append(0.0)
  
        if self.object.se_12_p2 == 'E': 
            table_data.append(0.25*1.0)
        elif self.object.se_12_p2 == 'D':
            table_data.append(0.25*0.8)
        elif self.object.se_12_p2 == 'C':
            table_data.append(0.25*0.65)
        elif self.object.se_12_p2 == 'B':
            table_data.append(0.25*0.5)
        else: # A o nulo
            table_data.append(0.0)
        #se 1.3
        if self.object.se_13_act == 'D': 
            table_data.append(0.25*1.0)
        elif self.object.se_13_act == 'C':
            table_data.append(0.25*0.7)
        elif self.object.se_13_act == 'B':
            table_data.append(0.25*0.5)
        else: # A o nulo
            table_data.append(0.0)

        if self.object.se_13_p1 == 'D': 
            table_data.append(0.25*1.0)
        elif self.object.se_13_p1 == 'C':
            table_data.append(0.25*0.7)
        elif self.object.se_13_p1 == 'B':
            table_data.append(0.25*0.5)
        else: # A o nulo
            table_data.append(0.0)
  
        if self.object.se_13_p2 == 'D': 
            table_data.append(0.25*1.0)
        elif self.object.se_13_p2 == 'C':
            table_data.append(0.25*0.7)
        elif self.object.se_13_p2 == 'B':
            table_data.append(0.25*0.5)
        else: # A o nulo
            table_data.append(0.0)
        #se 1.4
        if self.object.se_14_act == 'D': 
            table_data.append(0.1*1.0)
        elif self.object.se_14_act == 'C':
            table_data.append(0.1*0.7)
        elif self.object.se_14_act == 'B':
            table_data.append(0.1*0.5)
        else: # A o nulo
            table_data.append(0.0)

        if self.object.se_14_p1 == 'D': 
            table_data.append(0.1*1.0)
        elif self.object.se_14_p1 == 'C':
            table_data.append(0.1*0.7)
        elif self.object.se_14_p1 == 'B':
            table_data.append(0.1*0.5)
        else: # A o nulo
            table_data.append(0.0)
  
        if self.object.se_14_p2 == 'D': 
            table_data.append(0.1*1.0)
        elif self.object.se_14_p2 == 'C':
            table_data.append(0.1*0.7)
        elif self.object.se_14_p2 == 'B':
            table_data.append(0.1*0.5)
        else: # A o nulo
            table_data.append(0.0)
        #se 2.1
        if self.object.se_21_act == 'D': 
            table_data.append(0.2*1.0)
        elif self.object.se_21_act == 'C':
            table_data.append(0.2*0.5)
        elif self.object.se_21_act == 'B':
            table_data.append(0.2*0.3)
        else: # A o nulo
            table_data.append(0.0)

        if self.object.se_21_p1 == 'D': 
            table_data.append(0.2*1.0)
        elif self.object.se_21_p1 == 'C':
            table_data.append(0.2*0.5)
        elif self.object.se_21_p1 == 'B':
            table_data.append(0.2*0.3)
        else: # A o nulo
            table_data.append(0.0)
  
        if self.object.se_21_p2 == 'D': 
            table_data.append(0.2*1.0)
        elif self.object.se_21_p2 == 'C':
            table_data.append(0.2*0.5)
        elif self.object.se_21_p2 == 'B':
            table_data.append(0.2*0.3)
        else: # A o nulo
            table_data.append(0.0)
       #se 2.2
        if self.object.se_22_act == 'E': 
            table_data.append(0.25*1.0)
        elif self.object.se_22_act == 'D':
            table_data.append(0.25*0.7)
        elif self.object.se_22_act == 'C':
            table_data.append(0.25*0.5)
        elif self.object.se_22_act == 'B':
            table_data.append(0.25*0.3)
        else: # A o nulo
            table_data.append(0.0)

        if self.object.se_22_p1 == 'E': 
            table_data.append(0.25*1.0)
        elif self.object.se_22_p1 == 'D':
            table_data.append(0.25*0.7)
        elif self.object.se_22_p1 == 'C':
            table_data.append(0.25*0.5)
        elif self.object.se_22_p1 == 'B':
            table_data.append(0.25*0.3)
        else: # A o nulo
            table_data.append(0.0)
  
        if self.object.se_22_p2 == 'E': 
            table_data.append(0.25*1.0)
        elif self.object.se_22_p2 == 'D':
            table_data.append(0.25*0.7)
        elif self.object.se_22_p2 == 'C':
            table_data.append(0.25*0.5)
        elif self.object.se_22_p2 == 'B':
            table_data.append(0.25*0.3)
        else: # A o nulo
            table_data.append(0.0)
        #se 2.3
        if self.object.se_23_act == 'D': 
            table_data.append(0.2*1.0)
        elif self.object.se_23_act == 'C':
            table_data.append(0.2*0.5)
        elif self.object.se_23_act == 'B':
            table_data.append(0.2*0.3)
        else: # A o nulo
            table_data.append(0.0)

        if self.object.se_23_p1 == 'D': 
            table_data.append(0.2*1.0)
        elif self.object.se_23_p1 == 'C':
            table_data.append(0.2*0.5)
        elif self.object.se_23_p1 == 'B':
            table_data.append(0.2*0.3)
        else: # A o nulo
            table_data.append(0.0)
  
        if self.object.se_23_p2 == 'D': 
            table_data.append(0.2*1.0)
        elif self.object.se_23_p2 == 'C':
            table_data.append(0.2*0.5)
        elif self.object.se_23_p2 == 'B':
            table_data.append(0.2*0.3)
        else: # A o nulo
            table_data.append(0.0)
        #se 2.4
        if self.object.se_24_act == 'D': 
            table_data.append(0.18*1.0)
        elif self.object.se_24_act == 'C':
            table_data.append(0.18*0.7)
        elif self.object.se_24_act == 'B':
            table_data.append(0.18*0.3)
        else: # A o nulo
            table_data.append(0.0)

        if self.object.se_24_p1 == 'D': 
            table_data.append(0.18*1.0)
        elif self.object.se_24_p1 == 'C':
            table_data.append(0.18*0.7)
        elif self.object.se_24_p1 == 'B':
            table_data.append(0.18*0.3)
        else: # A o nulo
            table_data.append(0.0)
  
        if self.object.se_24_p2 == 'D': 
            table_data.append(0.18*1.0)
        elif self.object.se_24_p2 == 'C':
            table_data.append(0.18*0.7)
        elif self.object.se_24_p2 == 'B':
            table_data.append(0.18*0.3)
        else: # A o nulo
            table_data.append(0.0)
        #se 2.5
        if self.object.se_25_act == 'D': 
            table_data.append(0.17*1.0)
        elif self.object.se_25_act == 'C':
            table_data.append(0.17*0.7)
        elif self.object.se_25_act == 'B':
            table_data.append(0.17*0.3)
        else: # A o nulo
            table_data.append(0.0)

        if self.object.se_25_p1 == 'D': 
            table_data.append(0.17*1.0)
        elif self.object.se_25_p1 == 'C':
            table_data.append(0.17*0.7)
        elif self.object.se_25_p1 == 'B':
            table_data.append(0.17*0.3)
        else: # A o nulo
            table_data.append(0.0)
  
        if self.object.se_25_p2 == 'D': 
            table_data.append(0.17*1.0)
        elif self.object.se_25_p2 == 'C':
            table_data.append(0.17*0.7)
        elif self.object.se_25_p2 == 'B':
            table_data.append(0.17*0.3)
        else: # A o nulo
            table_data.append(0.0)
       #se 3.1
        if self.object.se_31_act == 'E': 
            table_data.append(0.25*1.0)
        elif self.object.se_31_act == 'D':
            table_data.append(0.25*0.7)
        elif self.object.se_31_act == 'C':
            table_data.append(0.25*0.5)
        elif self.object.se_31_act == 'B':
            table_data.append(0.25*0.3)
        else: # A o nulo
            table_data.append(0.0)

        if self.object.se_31_p1 == 'E': 
            table_data.append(0.25*1.0)
        elif self.object.se_31_p1 == 'D':
            table_data.append(0.25*0.7)
        elif self.object.se_31_p1 == 'C':
            table_data.append(0.25*0.5)
        elif self.object.se_31_p1 == 'B':
            table_data.append(0.25*0.3)
        else: # A o nulo
            table_data.append(0.0)
  
        if self.object.se_31_p2 == 'E': 
            table_data.append(0.25*1.0)
        elif self.object.se_31_p2 == 'D':
            table_data.append(0.25*0.7)
        elif self.object.se_31_p2 == 'C':
            table_data.append(0.25*0.5)
        elif self.object.se_31_p2 == 'B':
            table_data.append(0.25*0.3)
        else: # A o nulo
            table_data.append(0.0)
       #se 3.2
        if self.object.se_32_act == 'E': 
            table_data.append(0.25*1.0)
        elif self.object.se_32_act == 'D':
            table_data.append(0.25*0.7)
        elif self.object.se_32_act == 'C':
            table_data.append(0.25*0.3)
        elif self.object.se_32_act == 'B':
            table_data.append(0.25*0.1)
        else: # A o nulo
            table_data.append(0.0)

        if self.object.se_32_p1 == 'E': 
            table_data.append(0.25*1.0)
        elif self.object.se_32_p1 == 'D':
            table_data.append(0.25*0.7)
        elif self.object.se_32_p1 == 'C':
            table_data.append(0.25*0.3)
        elif self.object.se_32_p1 == 'B':
            table_data.append(0.25*0.1)
        else: # A o nulo
            table_data.append(0.0)
  
        if self.object.se_32_p2 == 'E': 
            table_data.append(0.25*1.0)
        elif self.object.se_32_p2 == 'D':
            table_data.append(0.25*0.7)
        elif self.object.se_32_p2 == 'C':
            table_data.append(0.25*0.3)
        elif self.object.se_32_p2 == 'B':
            table_data.append(0.25*0.1)
        else: # A o nulo
            table_data.append(0.0)
       #se 3.3
        if self.object.se_33_act == 'E': 
            table_data.append(0.25*1.0)
        elif self.object.se_33_act == 'D':
            table_data.append(0.25*0.7)
        elif self.object.se_33_act == 'C':
            table_data.append(0.25*0.3)
        elif self.object.se_33_act == 'B':
            table_data.append(0.25*0.1)
        else: # A o nulo
            table_data.append(0.0)

        if self.object.se_33_p1 == 'E': 
            table_data.append(0.25*1.0)
        elif self.object.se_33_p1 == 'D':
            table_data.append(0.25*0.7)
        elif self.object.se_33_p1 == 'C':
            table_data.append(0.25*0.3)
        elif self.object.se_33_p1 == 'B':
            table_data.append(0.25*0.1)
        else: # A o nulo
            table_data.append(0.0)
  
        if self.object.se_33_p2 == 'E': 
            table_data.append(0.25*1.0)
        elif self.object.se_33_p2 == 'D':
            table_data.append(0.25*0.7)
        elif self.object.se_33_p2 == 'C':
            table_data.append(0.25*0.3)
        elif self.object.se_33_p2 == 'B':
            table_data.append(0.25*0.1)
        else: # A o nulo
            table_data.append(0.0)
        #se 3.4
        if self.object.se_34_act == 'D': 
            table_data.append(0.25*1.0)
        elif self.object.se_34_act == 'C':
            table_data.append(0.25*0.7)
        elif self.object.se_34_act == 'B':
            table_data.append(0.25*0.5)
        else: # A o nulo
            table_data.append(0.0)

        if self.object.se_34_p1 == 'D': 
            table_data.append(0.25*1.0)
        elif self.object.se_34_p1 == 'C':
            table_data.append(0.25*0.7)
        elif self.object.se_34_p1 == 'B':
            table_data.append(0.25*0.5)
        else: # A o nulo
            table_data.append(0.0)
  
        if self.object.se_34_p2 == 'D': 
            table_data.append(0.25*1.0)
        elif self.object.se_34_p2 == 'C':
            table_data.append(0.25*0.7)
        elif self.object.se_34_p2 == 'B':
            table_data.append(0.25*0.5)
        else: # A o nulo
            table_data.append(0.0)
        #se 4.1
        if self.object.se_41_act == 'D': 
            table_data.append(0.2*1.0)
        elif self.object.se_41_act == 'C':
            table_data.append(0.2*0.7)
        elif self.object.se_41_act == 'B':
            table_data.append(0.2*0.5)
        else: # A o nulo
            table_data.append(0.0)

        if self.object.se_41_p1 == 'D': 
            table_data.append(0.2*1.0)
        elif self.object.se_41_p1 == 'C':
            table_data.append(0.2*0.7)
        elif self.object.se_41_p1 == 'B':
            table_data.append(0.2*0.5)
        else: # A o nulo
            table_data.append(0.0)
  
        if self.object.se_41_p2 == 'D': 
            table_data.append(0.2*1.0)
        elif self.object.se_41_p2 == 'C':
            table_data.append(0.2*0.7)
        elif self.object.se_41_p2 == 'B':
            table_data.append(0.2*0.5)
        else: # A o nulo
            table_data.append(0.0)
        #se 4.2
        if self.object.se_42_act == 'D': 
            table_data.append(0.2*1.0)
        elif self.object.se_42_act == 'C':
            table_data.append(0.2*0.7)
        elif self.object.se_42_act == 'B':
            table_data.append(0.2*0.5)
        else: # A o nulo
            table_data.append(0.0)

        if self.object.se_42_p1 == 'D': 
            table_data.append(0.2*1.0)
        elif self.object.se_42_p1 == 'C':
            table_data.append(0.2*0.7)
        elif self.object.se_42_p1 == 'B':
            table_data.append(0.2*0.5)
        else: # A o nulo
            table_data.append(0.0)
  
        if self.object.se_42_p2 == 'D': 
            table_data.append(0.2*1.0)
        elif self.object.se_42_p2 == 'C':
            table_data.append(0.2*0.7)
        elif self.object.se_42_p2 == 'B':
            table_data.append(0.2*0.5)
        else: # A o nulo
            table_data.append(0.0)
        #se 4.3
        if self.object.se_43_act == 'D': 
            table_data.append(0.2*1.0)
        elif self.object.se_43_act == 'C':
            table_data.append(0.2*0.5)
        elif self.object.se_43_act == 'B':
            table_data.append(0.2*0.3)
        else: # A o nulo
            table_data.append(0.0)

        if self.object.se_43_p1 == 'D': 
            table_data.append(0.2*1.0)
        elif self.object.se_43_p1 == 'C':
            table_data.append(0.2*0.5)
        elif self.object.se_43_p1 == 'B':
            table_data.append(0.2*0.3)
        else: # A o nulo
            table_data.append(0.0)
  
        if self.object.se_43_p2 == 'D': 
            table_data.append(0.2*1.0)
        elif self.object.se_43_p2 == 'C':
            table_data.append(0.2*0.5)
        elif self.object.se_43_p2 == 'B':
            table_data.append(0.2*0.3)
        else: # A o nulo
            table_data.append(0.0)
       #se 4.4
        if self.object.se_44_act == 'E': 
            table_data.append(0.2*1.0)
        elif self.object.se_44_act == 'D':
            table_data.append(0.2*0.7)
        elif self.object.se_44_act == 'C':
            table_data.append(0.2*0.5)
        elif self.object.se_44_act == 'B':
            table_data.append(0.2*0.3)
        else: # A o nulo
            table_data.append(0.0)

        if self.object.se_44_p1 == 'E': 
            table_data.append(0.2*1.0)
        elif self.object.se_44_p1 == 'D':
            table_data.append(0.2*0.7)
        elif self.object.se_44_p1 == 'C':
            table_data.append(0.2*0.5)
        elif self.object.se_44_p1 == 'B':
            table_data.append(0.2*0.3)
        else: # A o nulo
            table_data.append(0.0)
  
        if self.object.se_44_p2 == 'E': 
            table_data.append(0.2*1.0)
        elif self.object.se_44_p2 == 'D':
            table_data.append(0.2*0.7)
        elif self.object.se_44_p2 == 'C':
            table_data.append(0.2*0.5)
        elif self.object.se_44_p2 == 'B':
            table_data.append(0.2*0.3)
        else: # A o nulo
            table_data.append(0.0)
       #se 4.5
        if self.object.se_45_act == 'E': 
            table_data.append(0.2*1.0)
        elif self.object.se_45_act == 'D':
            table_data.append(0.2*0.7)
        elif self.object.se_45_act == 'C':
            table_data.append(0.2*0.5)
        elif self.object.se_45_act == 'B':
            table_data.append(0.2*0.3)
        else: # A o nulo
            table_data.append(0.0)

        if self.object.se_45_p1 == 'E': 
            table_data.append(0.2*1.0)
        elif self.object.se_45_p1 == 'D':
            table_data.append(0.2*0.7)
        elif self.object.se_45_p1 == 'C':
            table_data.append(0.2*0.5)
        elif self.object.se_45_p1 == 'B':
            table_data.append(0.2*0.3)
        else: # A o nulo
            table_data.append(0.0)
  
        if self.object.se_45_p2 == 'E': 
            table_data.append(0.2*1.0)
        elif self.object.se_45_p2 == 'D':
            table_data.append(0.2*0.7)
        elif self.object.se_45_p2 == 'C':
            table_data.append(0.2*0.5)
        elif self.object.se_45_p2 == 'B':
            table_data.append(0.2*0.3)
        else: # A o nulo
            table_data.append(0.0)
        #se 5.1
        if self.object.se_51_act == 'D': 
            table_data.append(0.35*1.0)
        elif self.object.se_51_act == 'C':
            table_data.append(0.35*0.7)
        elif self.object.se_51_act == 'B':
            table_data.append(0.35*0.5)
        else: # A o nulo
            table_data.append(0.0)

        if self.object.se_51_p1 == 'D': 
            table_data.append(0.35*1.0)
        elif self.object.se_51_p1 == 'C':
            table_data.append(0.35*0.7)
        elif self.object.se_51_p1 == 'B':
            table_data.append(0.35*0.5)
        else: # A o nulo
            table_data.append(0.0)
  
        if self.object.se_51_p2 == 'D': 
            table_data.append(0.35*1.0)
        elif self.object.se_51_p2 == 'C':
            table_data.append(0.35*0.7)
        elif self.object.se_51_p2 == 'B':
            table_data.append(0.35*0.5)
        else: # A o nulo
            table_data.append(0.0)
       #se 5.2
        if self.object.se_52_act == 'E': 
            table_data.append(0.35*1.0)
        elif self.object.se_52_act == 'D':
            table_data.append(0.35*0.7)
        elif self.object.se_52_act == 'C':
            table_data.append(0.35*0.5)
        elif self.object.se_52_act == 'B':
            table_data.append(0.35*0.3)
        else: # A o nulo
            table_data.append(0.0)

        if self.object.se_52_p1 == 'E': 
            table_data.append(0.35*1.0)
        elif self.object.se_52_p1 == 'D':
            table_data.append(0.35*0.7)
        elif self.object.se_52_p1 == 'C':
            table_data.append(0.35*0.5)
        elif self.object.se_52_p1 == 'B':
            table_data.append(0.35*0.3)
        else: # A o nulo
            table_data.append(0.0)
  
        if self.object.se_52_p2 == 'E': 
            table_data.append(0.35*1.0)
        elif self.object.se_52_p2 == 'D':
            table_data.append(0.35*0.7)
        elif self.object.se_52_p2 == 'C':
            table_data.append(0.35*0.5)
        elif self.object.se_52_p2 == 'B':
            table_data.append(0.35*0.3)
        else: # A o nulo
            table_data.append(0.0)
        #se 5.3
        if self.object.se_53_act == 'D': 
            table_data.append(0.3*1.0)
        elif self.object.se_53_act == 'C':
            table_data.append(0.3*0.7)
        elif self.object.se_53_act == 'B':
            table_data.append(0.3*0.3)
        else: # A o nulo
            table_data.append(0.0)

        if self.object.se_53_p1 == 'D': 
            table_data.append(0.3*1.0)
        elif self.object.se_53_p1 == 'C':
            table_data.append(0.3*0.7)
        elif self.object.se_53_p1 == 'B':
            table_data.append(0.3*0.3)
        else: # A o nulo
            table_data.append(0.0)
  
        if self.object.se_53_p2 == 'D': 
            table_data.append(0.3*1.0)
        elif self.object.se_53_p2 == 'C':
            table_data.append(0.3*0.7)
        elif self.object.se_53_p2 == 'B':
            table_data.append(0.3*0.3)
        else: # A o nulo
            table_data.append(0.0)

        return table_data

    def sum_results(self,srm, os, go, wam, tech, cust, vci, se):
        self.data_act = []
        self.data_p1 = []
        self.data_p2 = []
        self.prom_data_act = []
        self.prom_data_p1 = []
        self.prom_data_p2 = []
        ####SRM####
        i=0
        self.data_act.append(srm[0+i]+srm[3+i]+srm[6+i])
        self.data_act.append(srm[9+i]+srm[12+i]+srm[15+i]+srm[18+i]+srm[21+i]+srm[24+i])
        self.data_act.append(srm[27+i]+srm[30+i]+srm[33+i]+srm[36+i])
        self.data_act.append(srm[39+i]+srm[42+i]+srm[45+i])
        self.data_act.append(srm[48+i]+srm[51+i]+srm[54+i])
        i=1
        self.data_p1.append(srm[0+i]+srm[3+i]+srm[6+i])
        self.data_p1.append(srm[9+i]+srm[12+i]+srm[15+i]+srm[18+i]+srm[21+i]+srm[24+i])
        self.data_p1.append(srm[27+i]+srm[30+i]+srm[33+i]+srm[36+i])
        self.data_p1.append(srm[39+i]+srm[42+i]+srm[45+i])
        self.data_p1.append(srm[48+i]+srm[51+i]+srm[54+i])
        i=2
        self.data_p2.append(srm[0+i]+srm[3+i]+srm[6+i])
        self.data_p2.append(srm[9+i]+srm[12+i]+srm[15+i]+srm[18+i]+srm[21+i]+srm[24+i])
        self.data_p2.append(srm[27+i]+srm[30+i]+srm[33+i]+srm[36+i])
        self.data_p2.append(srm[39+i]+srm[42+i]+srm[45+i])
        self.data_p2.append(srm[48+i]+srm[51+i]+srm[54+i])

                ####OS####
        i=0
        self.data_act.append(os[0+i]+os[3+i]+os[6+i])
        self.data_act.append(os[9+i]+os[12+i]+os[15+i]+os[18+i]+os[21+i])
        self.data_act.append(os[24+i]+os[27+i]+os[30+i]+os[33+i]+os[36+i]+os[39+i])
        self.data_act.append(os[42+i]+os[45+i]+os[48+i])
        self.data_act.append(os[51+i]+os[54+i]+os[57+i])
        i=1
        self.data_p1.append(os[0+i]+os[3+i]+os[6+i])
        self.data_p1.append(os[9+i]+os[12+i]+os[15+i]+os[18+i]+os[21+i])
        self.data_p1.append(os[24+i]+os[27+i]+os[30+i]+os[33+i]+os[36+i]+os[39+i])
        self.data_p1.append(os[42+i]+os[45+i]+os[48+i])
        self.data_p1.append(os[51+i]+os[54+i]+os[57+i])
        i=2
        self.data_p2.append(os[0+i]+os[3+i]+os[6+i])
        self.data_p2.append(os[9+i]+os[12+i]+os[15+i]+os[18+i]+os[21+i])
        self.data_p2.append(os[24+i]+os[27+i]+os[30+i]+os[33+i]+os[36+i]+os[39+i])
        self.data_p2.append(os[42+i]+os[45+i]+os[48+i])
        self.data_p2.append(os[51+i]+os[54+i]+os[57+i])

                ####GO####
        i=0
        self.data_act.append(go[0+i]+go[3+i]+go[6+i]+go[9+i]+go[12+i])
        self.data_act.append(go[15+i]+go[18+i]+go[21+i]+go[24+i])
        self.data_act.append(go[27+i]+go[30+i]+go[33+i]+go[36+i]+go[39+i]+go[42+i])
        self.data_act.append(go[45+i]+go[48+i]+go[51+i]+go[54+i]+go[57+i])
        self.data_act.append(go[60+i]+go[63+i])
        i=1
        self.data_p1.append(go[0+i]+go[3+i]+go[6+i]+go[9+i]+go[12+i])
        self.data_p1.append(go[15+i]+go[18+i]+go[21+i]+go[24+i])
        self.data_p1.append(go[27+i]+go[30+i]+go[33+i]+go[36+i]+go[39+i]+go[42+i])
        self.data_p1.append(go[45+i]+go[48+i]+go[51+i]+go[54+i]+go[57+i])
        self.data_p1.append(go[60+i]+go[63+i])
        i=2
        self.data_p2.append(go[0+i]+go[3+i]+go[6+i]+go[9+i]+go[12+i])
        self.data_p2.append(go[15+i]+go[18+i]+go[21+i]+go[24+i])
        self.data_p2.append(go[27+i]+go[30+i]+go[33+i]+go[36+i]+go[39+i]+go[42+i])
        self.data_p2.append(go[45+i]+go[48+i]+go[51+i]+go[54+i]+go[57+i])
        self.data_p2.append(go[60+i]+go[63+i])

                ####WAM####
        i=0
        self.data_act.append(wam[0+i]+wam[3+i]+wam[6+i])
        self.data_act.append(wam[9+i]+wam[12+i]+wam[15+i])
        self.data_act.append(wam[18+i]+wam[21+i]+wam[24+i]+wam[27+i]+wam[30+i]+wam[33+i]+wam[36+i])
        self.data_act.append(wam[39+i]+wam[42+i]+wam[45+i]+wam[48+i])
        self.data_act.append(wam[51+i]+wam[54+i])
        i=1
        self.data_p1.append(wam[0+i]+wam[3+i]+wam[6+i])
        self.data_p1.append(wam[9+i]+wam[12+i]+wam[15+i])
        self.data_p1.append(wam[18+i]+wam[21+i]+wam[24+i]+wam[27+i]+wam[30+i]+wam[33+i]+wam[36+i])
        self.data_p1.append(wam[39+i]+wam[42+i]+wam[45+i]+wam[48+i])
        self.data_p1.append(wam[51+i]+wam[54+i])
        i=2
        self.data_p2.append(wam[0+i]+wam[3+i]+wam[6+i])
        self.data_p2.append(wam[9+i]+wam[12+i]+wam[15+i])
        self.data_p2.append(wam[18+i]+wam[21+i]+wam[24+i]+wam[27+i]+wam[30+i]+wam[33+i]+wam[36+i])
        self.data_p2.append(wam[39+i]+wam[42+i]+wam[45+i]+wam[48+i])
        self.data_p2.append(wam[51+i]+wam[54+i])

                ####TECH####
        i=0
        self.data_act.append(tech[0+i]+tech[3+i]+tech[6+i]+tech[9+i]+tech[12+i])
        self.data_act.append(tech[15+i]+tech[18+i]+tech[21+i]+tech[24+i]+tech[27+i]+tech[30+i]+tech[33+i])
        self.data_act.append(tech[36+i]+tech[39+i]+tech[42+i]+tech[45+i]+tech[48+i]+tech[51+i])
        self.data_act.append(tech[54+i]+tech[54+i]+tech[57+i]+tech[60+i]+tech[63+i]+tech[66+i]+tech[69+i])
        self.data_act.append(tech[72+i]+tech[75+i])
        i=1
        self.data_p1.append(tech[0+i]+tech[3+i]+tech[6+i]+tech[9+i]+tech[12+i])
        self.data_p1.append(tech[15+i]+tech[18+i]+tech[21+i]+tech[24+i]+tech[27+i]+tech[30+i]+tech[33+i])
        self.data_p1.append(tech[36+i]+tech[39+i]+tech[42+i]+tech[45+i]+tech[48+i]+tech[51+i])
        self.data_p1.append(tech[54+i]+tech[54+i]+tech[57+i]+tech[60+i]+tech[63+i]+tech[66+i]+tech[69+i])
        self.data_p1.append(tech[72+i]+tech[75+i])
        i=2
        self.data_p2.append(tech[0+i]+tech[3+i]+tech[6+i]+tech[9+i]+tech[12+i])
        self.data_p2.append(tech[15+i]+tech[18+i]+tech[21+i]+tech[24+i]+tech[27+i]+tech[30+i]+tech[33+i])
        self.data_p2.append(tech[36+i]+tech[39+i]+tech[42+i]+tech[45+i]+tech[48+i]+tech[51+i])
        self.data_p2.append(tech[54+i]+tech[54+i]+tech[57+i]+tech[60+i]+tech[63+i]+tech[66+i]+tech[69+i])
        self.data_p2.append(tech[72+i]+tech[75+i])

                ####CUST####
        i=0
        self.data_act.append(cust[0+i]+cust[3+i]+cust[6+i]+cust[9+i])
        self.data_act.append(cust[12+i]+cust[15+i]+cust[18+i]+cust[21+i]+cust[24+i]+cust[27+i])
        self.data_act.append(cust[30+i]+cust[33+i]+cust[36+i]+cust[39+i]+cust[42+i]+cust[45+i]+cust[48+i]+cust[51+i]+cust[54+i])
        self.data_act.append(cust[57+i]+cust[60+i]+cust[63+i]+cust[66+i]+cust[69+i]+cust[72+i]+cust[75+i])
        self.data_act.append(cust[78+i]+cust[81+i]+cust[84+i]+cust[87+i]+cust[90+i])
        i=1
        self.data_p1.append(cust[0+i]+cust[3+i]+cust[6+i]+cust[9+i])
        self.data_p1.append(cust[12+i]+cust[15+i]+cust[18+i]+cust[21+i]+cust[24+i]+cust[27+i])
        self.data_p1.append(cust[30+i]+cust[33+i]+cust[36+i]+cust[39+i]+cust[42+i]+cust[45+i]+cust[48+i]+cust[51+i]+cust[54+i])
        self.data_p1.append(cust[57+i]+cust[60+i]+cust[63+i]+cust[66+i]+cust[69+i]+cust[72+i]+cust[75+i])
        self.data_p1.append(cust[78+i]+cust[81+i]+cust[84+i]+cust[87+i]+cust[90+i])
        i=2
        self.data_p2.append(cust[0+i]+cust[3+i]+cust[6+i]+cust[9+i])
        self.data_p2.append(cust[12+i]+cust[15+i]+cust[18+i]+cust[21+i]+cust[24+i]+cust[27+i])
        self.data_p2.append(cust[30+i]+cust[33+i]+cust[36+i]+cust[39+i]+cust[42+i]+cust[45+i]+cust[48+i]+cust[51+i]+cust[54+i])
        self.data_p2.append(cust[57+i]+cust[60+i]+cust[63+i]+cust[66+i]+cust[69+i]+cust[72+i]+cust[75+i])
        self.data_p2.append(cust[78+i]+cust[81+i]+cust[84+i]+cust[87+i]+cust[90+i])


                ####VCI####
        i=0
        self.data_act.append(vci[0+i]+vci[3+i]+vci[6+i]+vci[9+i]+vci[12+i])
        self.data_act.append(vci[15+i]+vci[18+i]+vci[21+i]+vci[24+i])
        self.data_act.append(vci[27+i]+vci[30+i]+vci[33+i]+vci[36+i])
        self.data_act.append(vci[39+i]+vci[42+i]+vci[45+i]+vci[48+i])
        self.data_act.append(vci[51+i]+vci[54+i]+vci[57+i])

        i=1
        self.data_p1.append(vci[0+i]+vci[3+i]+vci[6+i]+vci[9+i]+vci[12+i])
        self.data_p1.append(vci[15+i]+vci[18+i]+vci[21+i]+vci[24+i])
        self.data_p1.append(vci[27+i]+vci[30+i]+vci[33+i]+vci[36+i])
        self.data_p1.append(vci[39+i]+vci[42+i]+vci[45+i]+vci[48+i])
        self.data_p1.append(vci[51+i]+vci[54+i]+vci[57+i])

        i=2
        self.data_p2.append(vci[0+i]+vci[3+i]+vci[6+i]+vci[9+i]+vci[12+i])
        self.data_p2.append(vci[15+i]+vci[18+i]+vci[21+i]+vci[24+i])
        self.data_p2.append(vci[27+i]+vci[30+i]+vci[33+i]+vci[36+i])
        self.data_p2.append(vci[39+i]+vci[42+i]+vci[45+i]+vci[48+i])
        self.data_p2.append(vci[51+i]+vci[54+i]+vci[57+i])


                ####SE####
        i=0
        self.data_act.append(se[0+i]+se[3+i]+se[6+i]+se[9+i])
        self.data_act.append(se[12+i]+se[15+i]+se[18+i]+se[21+i]+se[24+i])
        self.data_act.append(se[27+i]+se[30+i]+se[33+i]+se[36+i])
        self.data_act.append(se[39+i]+se[42+i]+se[45+i]+se[48+i]+se[51+i])
        self.data_act.append(se[54+i]+se[57+i]+se[60+i])
        i=1
        self.data_p1.append(se[0+i]+se[3+i]+se[6+i]+se[9+i])
        self.data_p1.append(se[12+i]+se[15+i]+se[18+i]+se[21+i]+se[24+i])
        self.data_p1.append(se[27+i]+se[30+i]+se[33+i]+se[36+i])
        self.data_p1.append(se[39+i]+se[42+i]+se[45+i]+se[48+i]+se[51+i])
        self.data_p1.append(se[54+i]+se[57+i]+se[60+i])
        i=2
        self.data_p2.append(se[0+i]+se[3+i]+se[6+i]+se[9+i])
        self.data_p2.append(se[12+i]+se[15+i]+se[18+i]+se[21+i]+se[24+i])
        self.data_p2.append(se[27+i]+se[30+i]+se[33+i]+se[36+i])
        self.data_p2.append(se[39+i]+se[42+i]+se[45+i]+se[48+i]+se[51+i])
        self.data_p2.append(se[54+i]+se[57+i]+se[60+i])


        #PROMEDIOS
        self.prom_data_act.append((self.data_act[0]+self.data_act[1]+self.data_act[2]+self.data_act[3]+self.data_act[4])/5)
        self.prom_data_act.append((self.data_act[5]+self.data_act[6]+self.data_act[7]+self.data_act[8]+self.data_act[9])/5)
        self.prom_data_act.append((self.data_act[10]+self.data_act[11]+self.data_act[12]+self.data_act[13]+self.data_act[14])/5)
        self.prom_data_act.append((self.data_act[15]+self.data_act[16]+self.data_act[17]+self.data_act[18]+self.data_act[19])/5)
        self.prom_data_act.append((self.data_act[20]+self.data_act[21]+self.data_act[22]+self.data_act[23]+self.data_act[24])/5)
        self.prom_data_act.append((self.data_act[25]+self.data_act[26]+self.data_act[27]+self.data_act[28]+self.data_act[29])/5)
        self.prom_data_act.append((self.data_act[30]+self.data_act[31]+self.data_act[32]+self.data_act[33]+self.data_act[34])/5)
        self.prom_data_act.append((self.data_act[35]+self.data_act[36]+self.data_act[37]+self.data_act[38]+self.data_act[39])/5)
        self.prom_data_act.append((self.prom_data_act[0]+self.prom_data_act[1]+self.prom_data_act[2]+self.prom_data_act[3]+self.prom_data_act[4]+self.prom_data_act[5]+self.prom_data_act[6]+self.prom_data_act[7])/8)

        self.prom_data_p1.append((self.data_p1[0]+self.data_p1[1]+self.data_p1[2]+self.data_p1[3]+self.data_p1[4])/5)
        self.prom_data_p1.append((self.data_p1[5]+self.data_p1[6]+self.data_p1[7]+self.data_p1[8]+self.data_p1[9])/5)
        self.prom_data_p1.append((self.data_p1[10]+self.data_p1[11]+self.data_p1[12]+self.data_p1[13]+self.data_p1[14])/5)
        self.prom_data_p1.append((self.data_p1[15]+self.data_p1[16]+self.data_p1[17]+self.data_p1[18]+self.data_p1[19])/5)
        self.prom_data_p1.append((self.data_p1[20]+self.data_p1[21]+self.data_p1[22]+self.data_p1[23]+self.data_p1[24])/5)
        self.prom_data_p1.append((self.data_p1[25]+self.data_p1[26]+self.data_p1[27]+self.data_p1[28]+self.data_p1[29])/5)
        self.prom_data_p1.append((self.data_p1[30]+self.data_p1[31]+self.data_p1[32]+self.data_p1[33]+self.data_p1[34])/5)
        self.prom_data_p1.append((self.data_p1[35]+self.data_p1[36]+self.data_p1[37]+self.data_p1[38]+self.data_p1[39])/5)
        self.prom_data_p1.append((self.prom_data_p1[0]+self.prom_data_p1[1]+self.prom_data_p1[2]+self.prom_data_p1[3]+self.prom_data_p1[4]+self.prom_data_p1[5]+self.prom_data_p1[6]+self.prom_data_p1[7])/8)

        self.prom_data_p2.append((self.data_p2[0]+self.data_p2[1]+self.data_p2[2]+self.data_p2[3]+self.data_p2[4])/5)
        self.prom_data_p2.append((self.data_p2[5]+self.data_p2[6]+self.data_p2[7]+self.data_p2[8]+self.data_p2[9])/5)
        self.prom_data_p2.append((self.data_p2[10]+self.data_p2[11]+self.data_p2[12]+self.data_p2[13]+self.data_p2[14])/5)
        self.prom_data_p2.append((self.data_p2[15]+self.data_p2[16]+self.data_p2[17]+self.data_p2[18]+self.data_p2[19])/5)
        self.prom_data_p2.append((self.data_p2[20]+self.data_p2[21]+self.data_p2[22]+self.data_p2[23]+self.data_p2[24])/5)
        self.prom_data_p2.append((self.data_p2[25]+self.data_p2[26]+self.data_p2[27]+self.data_p2[28]+self.data_p2[29])/5)
        self.prom_data_p2.append((self.data_p2[30]+self.data_p2[31]+self.data_p2[32]+self.data_p2[33]+self.data_p2[34])/5)
        self.prom_data_p2.append((self.data_p2[35]+self.data_p2[36]+self.data_p2[37]+self.data_p2[38]+self.data_p2[39])/5)
        self.prom_data_p2.append((self.prom_data_p2[0]+self.prom_data_p2[1]+self.prom_data_p2[2]+self.prom_data_p2[3]+self.prom_data_p2[4]+self.prom_data_p2[5]+self.prom_data_p2[6]+self.prom_data_p2[7])/8)
     
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        table_srm = self.get_table_data_srm()
        table_os = self.get_table_data_os()
        table_go = self.get_table_data_go()
        table_wam = self.get_table_data_wam()
        table_tech = self.get_table_data_tech()
        table_cust = self.get_table_data_cust()
        table_vci = self.get_table_data_vci()
        table_se = self.get_table_data_se()

        self.sum_results(table_srm, table_os, table_go, table_wam, table_tech, table_cust, table_vci, table_se)

        context['dataAct'] = [ '%.2f' % elem for elem in self.data_act ]
        context['dataP1'] = [ '%.2f' % elem for elem in self.data_p1 ]
        context['dataP2'] =  [ '%.2f' % elem for elem in self.data_p2 ]
        context['P_dataAct'] = [ '%.2f' % elem for elem in self.prom_data_act ]
        context['P_dataP1'] = [ '%.2f' % elem for elem in self.prom_data_p1 ]
        context['P_dataP2'] = [ '%.2f' % elem for elem in self.prom_data_p2 ]
        return context

###################################################################
###################################################################


class QuestionaryCreate(CreateView):
    model = Questionary
    form_class = QuestionaryForm
    
    def get_success_url(self):
        return reverse_lazy('questionaries:questionary', args=[self.object.id, slugify(self.object.name)]) 

class QuestionaryUpdate(UpdateView):
    model = Questionary
    form_class = QuestionaryUpdateForm
    template_name_suffix = '_update_form'

    def get_success_url(self):
        return reverse_lazy('questionaries:update_OS', args=[self.object.id]) + '?ok'

class QuestionaryUpdate_OS(UpdateView):
    model = Questionary
    form_class = QuestionaryUpdateForm
    template_name_suffix = '_update_form_OS'

    def get_success_url(self):
        return reverse_lazy('questionaries:update_GO', args=[self.object.id]) + '?ok'

class QuestionaryUpdate_GO(UpdateView):
    model = Questionary
    form_class = QuestionaryUpdateForm
    template_name_suffix = '_update_form_GO'

    def get_success_url(self):
        return reverse_lazy('questionaries:update_WAM', args=[self.object.id]) + '?ok'

class QuestionaryUpdate_WAM(UpdateView):
    model = Questionary
    form_class = QuestionaryUpdateForm
    template_name_suffix = '_update_form_WAM'

    def get_success_url(self):
        return reverse_lazy('questionaries:update_TECH', args=[self.object.id]) + '?ok'

class QuestionaryUpdate_TECH(UpdateView):
    model = Questionary
    form_class = QuestionaryUpdateForm
    template_name_suffix = '_update_form_TECH'

    def get_success_url(self):
        return reverse_lazy('questionaries:update_CUST', args=[self.object.id]) + '?ok'

class QuestionaryUpdate_CUST(UpdateView):
    model = Questionary
    form_class = QuestionaryUpdateForm
    template_name_suffix = '_update_form_CUST'

    def get_success_url(self):
        return reverse_lazy('questionaries:update_VCI', args=[self.object.id]) + '?ok'

class QuestionaryUpdate_VCI(UpdateView):
    model = Questionary
    form_class = QuestionaryUpdateForm
    template_name_suffix = '_update_form_VCI'

    def get_success_url(self):
        return reverse_lazy('questionaries:update_SE', args=[self.object.id]) + '?ok'

class QuestionaryUpdate_SE(UpdateView):
    model = Questionary
    form_class = QuestionaryUpdateForm
    template_name_suffix = '_update_form_SE'

    def get_success_url(self):
        return reverse_lazy('questionaries:questionary', args=[self.object.id, slugify(self.object.name)]) + '?ok'


class QuestionaryDelete(DeleteView):
    model = Questionary
    success_url = reverse_lazy('questionaries:questionaries')