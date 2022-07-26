import math as m, numpy as np
import matplotlib.pyplot as plt
from soil_plot import Soils
languages = {
  'EN': [
"\nEnter the values of the soil by mesh. If there is a value you don't have, write 'None' or press Enter ",
"Grams for",
"No negative values.",
"That is not a number",
"What is the weight of the total mass?",
"Really -.-?",
"Which analysis would you like to run?\n    1. Sieve Analysis\n    2. Plasticity Analysis\n    3. Both",
"Your input mass has to be greater or equal than the sum of all your input weights. Reintroduce your data.",
"LGTM!",
"Bottom",
"Input your laboratory data through Casagrande's method with the following order and a space between. Everything with the same units.\n    #Hits\tID\tWeight recipient\tWeight recipient+wet soil\tWeight recipient+dried soil",
"Input your laboratory data of the plastic limit. Everything with the same units.\n    ID\tWeight recipient\tWeight recipient+wet soil\tWeight recipient+dried soil",
"s",# 12
"Please write the following data \n",
"Building Name: ",
"Depth: ",
"Location: ",
"Sample: ",
"Description: ",
"Standard: ",
"Date: ",
"Reviewed: ",
"Made By: ",
"You need to give at leat 2 samples.",
"Not a valid input. Example: 19 UY-8f 72.5 80.3 74.3",
"Not a valid input. Example: 19 UY-8f 72.5 80.3 74.3"
],

  'ES': [
"\nIntroduzca los valores del suelo por malla. Si hay un valor que no tenga, escriba 'None' o presione Enter.", # 0
"Gramos para", # 1
"No valores negativos.", # 2
"Eso no es un número", # 3
"¿Cuál es el peso total de la masa?", # 4
"¿Enserio -.-?", # 5
"¿Qué análisis desea realizar?\n    1. Análisis granulométrico\n    2. Análisis de plasticidad\n    3. Ambos", # 6
"Su masa introducida debe ser mayor o igual a la suma de todos los pesos de las mallas. Reintroduzca sus datos.", # 7
"Todo en orden", # 8
"Fondo", # 9
"Introduzca sus datos de laboratorio del método de Casagrande en el siguiente orden separados por un espacio. Todo en las mismas unidades.\n    #Golpes\tID\tPeso cápsula\tPeso cápsula+suelo húmedo\tPeso cápsula+suelo seco", # 10
"Introduzca sus datos de laboratorio del límite plástico. Todo en las mismas unidades.\n    ID\tPeso cápsula\tPeso cápsula+suelo húmedo\tPeso cápsula+suelo seco", # 11
"s",# 12
"Por favor ingrese sus datos \n",
"Nombre de la Obra: ",
"Profundidad: ",
"Localización: ",
"Muestra: ",
"Descripción: ",
"Norma: ",
"Fecha: ",
"Revisó: ",
"Elaboró: ",
"Debe poner al menos 2 muestras.",
"No es válido. Ejemplo: 19 UY-8f 72.5 80.3 74.3",
"No es válido. Ejemplo: 19 UY-8f 72.5 80.3 74.3",
],

  '中文': [
"\n通过网格输入土壤的值。如果你没有的号码, 写《None》或按 Enter。",
"网格克数",
"没有负数。", 
"那不是一个数字。",
"样品的总重量是多少?",
"真的吗 -.-?",
"您要运行哪种分析?\n    一. 筲箕的分析\n    二. 塑性变形的分析\n    三. 都",
"您输入的数据必须大于或等于您输入的所有权重的总和。 请重新输入您的数据。",
"好不错",
"底部",
"输入您通过 Casagrande 方法测量的数据。请按以下顺序写入数据，中间有空格。一切都具有相同的单位。\n    #打\tID\t碗的重量\t碗的重量+湿的样品\t碗的重量+干燥样品",
"输入阿特贝限的详细信息。一切都具有相同的单位。\n    ID\t碗的重量\t碗的重量+湿的样品\t碗的重量+干燥样品",
"s",# 12
"请输入您的数据 \n",
"建造的名字: ",
"深度: ",
"地点: ",
"样本: ",
"描述: ",
"标准: ",
"日期: ",
"审核: ",
"做的: ",
"您需要提供至少 2 个样本",
"无效。例子：19 UY-8f 72.5 80.3 74.3"
],
}  

def sieveData(yu):
  mesh = {'4"':101.6, '3"':76.2, '2"':50.8, '1"':25.4, '3/4"':19.1, '1/2"':12.7, '3/8"':9.52, '1/4"':6.35, '4':4.76, '6':3.36, '8':2.38, '10':2, '12':1.68, '16':1.19, '20':0.84, '30':0.59, '40':0.42, '50':0.297, '60':0.25, '70':0.21, '100':0.149, '140':0.105, '200':0.074, '270':0.053, '400':0.037}
  global languages
  sentences = languages[yu]
  
  print(f"    {sentences[0]}")
  
  ############# Getting Soil Data #############
  
  use_mesh = dict()
  x_axis, x_axis_name = list(), list()

  for i,h in mesh.items():
    while True:
      value = input(f"    {sentences[1]} {i}: ")
      if value == 'None' or value == '':
        break
      try:
        value = float(value)
        if value < 0:
          print(f"    {sentences[2]}")
        else:
          use_mesh[mesh[i]] = value
          x_axis.append(mesh[i])
          x_axis_name.append(i)
          break
      except:
        print(f"    {sentences[3]}")
  
  sum_mass = 0
  for i, j in use_mesh.items():
    sum_mass += j

  ############# Asking for the Mass #############
  print(f'    Σ = {sum_mass} g')
  while True:
    mass = input(f'    {sentences[4]}: ')
    try:
      mass = float(mass)
      if mass < 0:
        print(f'    {sentences[2]}')
        continue
      elif mass == 0:
        print(f'    {sentences[5]}')
      else: 
        break
    except:
      print(f'    {sentences[3]}')

  ############# Checking Total Mass #############
  if sum_mass > mass:
    print(f'    {sentences[7]}')
    return sieveData(yu)
  else:
    print(f'    {sentences[8]}')
    return use_mesh, mass, mass - sum_mass, x_axis_name

def pdata(yu):
  global languages
  sentences = languages[yu]

  print(f"   {sentences[13]}")
  obra = str(input(f"    {sentences[14]}"))
  profundidad = str(input(f"    {sentences[15]}"))
  localizacion = str(input(f"    {sentences[16]}"))
  muestra = str(input(f"    {sentences[17]}"))
  descripcion = str(input(f"    {sentences[18]}"))
  norma = str(input(f"    {sentences[19]}"))
  fecha = str(input(f"    {sentences[20]}"))
  reviso = str(input(f"    {sentences[21]}"))
  elaboro = str(input(f"    {sentences[22]}"))
  return {'obra':obra, 'profundidad': profundidad, 'localizacion':localizacion, 'muestra':muestra, 'descripcion':descripcion, 'norma':norma, 'fecha':fecha, 'reviso':reviso, 'elaboro':elaboro}

def plasticData(yu):

  global languages
  sentences = languages[yu]
  ll_data, pl_data = [], []

  print(f"    {sentences[10]}")
  counter = 0
  while True:

    ans = str(input(f"    --> "))
    if ans.lower() == "exit":
      if counter >= 2: 
        break
      print(f"    {sentences[23]}")
    
    ans, good = ans.split(), list()

    if len(ans) < 5 or len(ans) > 5:
      print(f"    {sentences[24]}")
      continue
    
    for j, i in enumerate(ans):
      if j == 1:
        good.append(i)
        continue
      try:
        i = float(i)
        good.append(i)
      except:
        break
    else:
      counter += 1
      ll_data.append(good)
      if 6 == counter: break
      continue
  
  print(f"    {sentences[11]}")
  counter = 0
  while True:

    ans = str(input(f"    --> "))
    ans, good = ans.split(), list()

    if len(ans) < 4 or len(ans) > 4:
      print(f"    {sentences[25]}")
      continue

    for j, i in enumerate(ans):
      if j == 0: 
        good.append(i)
        continue
      try:
        i = float(i)
        good.append(i)
      except:
        break
    else:
      counter += 1
      pl_data.append(good)
      if 2 == counter: break
      continue
  return ll_data, pl_data

def plot_Plasticity(ll, ip):
  import matplotlib.pyplot as plt

  fig, ax = plt.subplots()
  ax.plot(ll, ip, 'cyan', marker="D", figure= fig)
  ax.xaxis.grid()
  ax.grid(True)
  plt.ylim(0)
  if ll < 50:
    limright = 70
    plt.xlim([0, limright])
    ax.plot([20, 70], [0, ((11 / 15) * (70 - 20))], 'b', marker="")
  else:
    plt.xlim([0, ll + 20])
    ax.plot([20, ll + 20], [0, ((11 / 15) * (ll))], 'b', marker="")
  fig.tight_layout()
  return fig

def plot_Hits(hits, wc, eq, x, y):
  cycle3 = list(np.linspace(1,10,10))
  cycle4 = list(np.linspace(10,100,10))

  fig, ax = plt.subplots()

  plt.xscale("log")
  ax.plot(x, y, linestyle='', color='b', marker="o",)
  ax.plot(hits, wc, linestyle='--', color='b', label=f'$f(x)= {round(eq[0],2)} \;\log (x) + {round(eq[1],2)}$')
  plt.legend()
  plt.gca().set_xticks(cycle3 + cycle4, minor=False)
  ax.xaxis.grid()
  ax.grid(True)
  plt.xlim(1,100)
  fig.tight_layout()
  return fig

def plot_Sieves(mesh, passing, d60, d30, d10):
  cycle1 = list(np.linspace(0.01,0.1,10))
  cycle2 = list(np.linspace(0.1,1,10))
  cycle3 = list(np.linspace(1,10,10))
  cycle4 = list(np.linspace(10,100,10))
  main_cycle = cycle1 + cycle2 + cycle3 + cycle4
  y_ticks = range(0,101,10)

  fig, ax = plt.subplots()

  plt.xscale("log")
  ax.plot(mesh, passing, 'b', marker="o")
  if type(d60) != type(str("sad")):
    ax.plot(d60, 60, color= "cyan", marker="D")
    ax.plot(d30, 30, color= "cyan", marker="D")
    ax.plot(d10, 10, color= "cyan", marker="D")
  ax.set_xticks(main_cycle, minor=False)
  ax.set_yticks(y_ticks, minor=False)
  ax.plot([4.76, 4.76], [0, 100], color='r', linestyle='--')
  ax.plot([0.074, 0.074], [0, 100], color='r', linestyle='--')
  ax.xaxis.grid()
  ax.grid(True)
  ax.invert_xaxis()
  plt.xlim(100,0.01)
  plt.ylim(0, 100)
  fig.tight_layout()
  return fig

def main():

  #############  LANGUAGE  #############
  
  print(f"    1. EN\n    2. ES\n    3. 中文")
  lang = str(input("    --> "))
  
  if lang == '1' or lang == 'EN': lang = 'EN'	
  elif lang == '2' or lang == 'ES': lang = 'ES'
  elif lang == '3' or lang == '中文': lang = '中文'
  else: return main()
  
  global languages
  sentences = languages[lang] 

  ############# FORM DATA #############

  form_data = pdata(lang)

  ############# ANALISIS TYPE #############
  
  print(f"    {sentences[6]}")
  resp = str(input("    --> "))
  
  while True:
    if resp == '1' or resp == '2' or resp == '3': break
    resp = str(input("    --> "))
  
  ############# POWERFUL STUFF COMING #############
  from pdf_soil import Pdf_soil
  import os
  if resp == '1':
    sieve = sieveData(lang)
    use_mesh = sieve[0]
    peso_ret = list()
    for i, j in use_mesh.items():
      peso_ret.append(j)
    a = Soils(use_mesh, sieve[1])
    diam = a.d136()
    presucs = a.sucs_pre()

    datos = {'mesh': a.mesh, 'mesh_name': sieve[3], 'passing': a.passing, 'peso_ret': peso_ret, 'cu': diam['cu'] , 'cc': diam['cc'], 'sand': presucs['sand'], 'gravel': presucs['gravel'], 'fines': presucs['fines'], 'sucs': presucs['sucs'], 'd60': diam['d60'], 'd30': diam['d30'], 'd10': diam['d10']}

    fig_sieve = plot_Sieves(datos['mesh'], datos['passing'], datos['d60'], datos['d30'], datos['d10'])
    plt.savefig("fig_sieve.png", dpi= 300,format='png')
    Pdf_soil().Sieve_PDF(form_data, datos, lang)
    os.remove("fig_sieve.png")

  elif resp == '2':
    atterberg = plasticData(lang)
    a = Soils({2:[2,4], 3:[2,4]}, 7)
    plast = a.plasticity(atterberg[0], atterberg[1])
    datos = {'Fw' : plast['fw'], 'cte' : plast['cte'], 'Ip' : plast['Ip'], 'IpA' : plast['IpA'], 'll' : plast['ll'], 'pl' : plast['pl'], 'sucs' : plast['sucs'], 'hits' : plast['hits'], 'wc' : plast['wc'], 'x' : plast['x'], 'y' : plast['y'], 'lld': plast['lld'], 'pld': plast['pld']}
    fig_hits = plot_Hits(datos['hits'], datos['wc'], [datos['Fw'], datos['cte']], datos['x'], datos['y'])
    plt.savefig("fig_hits.png", dpi=300, format='png')
    fig_plast = plot_Plasticity(datos['ll'], datos['Ip'])
    plt.savefig("fig_plast.png", dpi=300, format='png')
    Pdf_soil().Plast_PDF(form_data, datos, lang)
    os.remove("fig_plast.png")
    os.remove("fig_hits.png")
  else:
    sieve = sieveData(lang)
    atterberg = plasticData(lang)
    
    use_mesh = sieve[0]
    peso_ret = list()
    for i, j in use_mesh.items():
      peso_ret.append(j)
    a = Soils(use_mesh, sieve[1])
    diam = a.d136()
    presucs = a.sucs_pre()

    datos = {'mesh': a.mesh, 'mesh_name': sieve[3], 'passing': a.passing, 'peso_ret': peso_ret, 'cu': diam['cu'] , 'cc': diam['cc'], 'sand': presucs['sand'], 'gravel': presucs['gravel'], 'fines': presucs['fines'], 'sucs': presucs['sucs'], 'd60': diam['d60'], 'd30': diam['d30'], 'd10': diam['d10']}

    plast = a.plasticity(atterberg[0], atterberg[1])
    datos_pl = {'Fw' : plast['fw'], 'cte' : plast['cte'], 'Ip' : plast['Ip'], 'IpA' : plast['IpA'], 'll' : plast['ll'], 'pl' : plast['pl'], 'sucs' : plast['sucs'], 'hits' : plast['hits'], 'wc' : plast['wc'], 'x' : plast['x'], 'y' : plast['y'], 'lld': plast['lld'], 'pld': plast['pld']}

    fig_sieve = plot_Sieves(datos['mesh'], datos['passing'], datos['d60'], datos['d30'], datos['d10'])
    plt.savefig("fig_sieve.png", dpi= 300,format='png')
    fig_hits = plot_Hits(datos_pl['hits'], datos_pl['wc'], [datos_pl['Fw'], datos_pl['cte']], datos_pl['x'], datos_pl['y'])
    plt.savefig("fig_hits.png", dpi=300, format='png')
    fig_plast = plot_Plasticity(datos_pl['ll'], datos_pl['Ip'])
    plt.savefig("fig_plast.png", dpi=300, format='png')
    Pdf_soil().Sieve_PDF(form_data, datos, lang)
    Pdf_soil().Plast_PDF(form_data, datos_pl, lang)
    os.remove("fig_sieve.png")
    os.remove("fig_plast.png")
    os.remove("fig_hits.png")
  
main()