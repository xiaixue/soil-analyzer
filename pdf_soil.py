languages = {
  'EN': [['SIEVE ANALYSIS', 'Building Name:', 'Location:', 'Depth:', 'Sample:', 'By:', 'Date:', "Mesh", "W. Ret. (g)", "% passes", "Sand", "Gravel", "Fines", 'Mesh Diameter [mm]', 'Hit Number', "ATTERBERG ANALYSIS", "Hits", "ID", "Wr", "Wr+w", "Wr+s", "Ww", "Ws", "w(%)", "Liquid Limit", "Plastic Limit"]],
  'ES': [['ANÁLISIS DE GRANULOMETRÍA', 'Obra:', 'Localización:', 'Profundidad:', 'Muestra:', 'Elaboró:', 'Fecha:', "Malla", "W. Ret. (g)", "% que pasa", "Arenas", "Gravas", "Finos", 'Diámetro de malla [mm]', 'Número de Golpes', "ANÁLISIS DE CONSISTENCIA","Golpes", "ID", "Wr", "Wr+w", "Wr+s", "Ww", "Ws", "w(%)", "Límite Líquido", "Límite Plástico"]], #12
  '中文': [['SIEVE ANALYSIS', 'Building Name:', 'Location:', 'Depth:', 'Sample:', 'By:', 'Date:', "Mesh", "W. Ret. (g)", "% passes", "Sand", "Gravel", "Fines", 'Mesh Diameter [mm]', 'Hit Number', "ATTERBERG ANALYSIS", "Hits", "ID", "Wr", "Wr+w", "Wr+s", "Ww", "Ws", "w(%)", "Liquid Limit", "Plastic Limit"]],
}  

class Pdf_soil():
  def Sieve_PDF(self, form_data, datos, yu):
    from fpdf import FPDF
    import fpdf

    global languages
    sentences = languages[yu]
    f = 0
    name_titulo = sentences[f][0]
    name_obra = sentences[f][1]
    name_location = sentences[f][2]
    name_depth = sentences[f][3]
    name_sample = sentences[f][4]
    name_author = sentences[f][5]
    name_date = sentences[f][6]
    name_mesh = sentences[f][7]
    name_wret = sentences[f][8]
    name_passes = sentences[f][9]
    name_sand = sentences[f][10]
    name_gravel = sentences[f][11]
    name_fines = sentences[f][12]
    name_xaxis = sentences[f][13]
    
    pdf = FPDF(orientation = 'P', unit = 'mm', format=(297,210))
    pdf.add_page()
    pdf.set_font('Helvetica', '', 12)
    pdf.set_fill_color(217, 217, 217)
    d_cell_h, d_cell_b = 6.6145833325, 42.333333328
    pdf.set_xy(95 - d_cell_b * 2, 16.5 - d_cell_h)
    pdf.cell(d_cell_b * 2, h = d_cell_h * 3 , txt = name_titulo, border = 1, ln = 0, align = 'C', fill = True)
    pdf.set_xy(95, 16.5 - d_cell_h)
    pdf.cell(d_cell_b, d_cell_h , txt = name_obra, border = 1, ln = 0, align = 'R', fill = True)
    pdf.set_xy(95, 16.5)
    pdf.cell(d_cell_b, d_cell_h , txt = name_location, border = 1, ln = 0, align = 'R', fill = True)
    pdf.set_xy(95, 16.5 + d_cell_h)
    pdf.cell(d_cell_b, d_cell_h , txt = name_depth, border = 1, ln = 0, align = 'R', fill = True)
    pdf.set_xy(95 + 2 * d_cell_b, 16.5-d_cell_h)
    pdf.cell(d_cell_b, d_cell_h , txt = name_sample, border = 1, ln = 0, align = 'R', fill = True)
    pdf.set_xy(95 + 2 * d_cell_b, 16.5)
    pdf.cell(d_cell_b, d_cell_h , txt = name_author, border = 1, ln = 0, align = 'R', fill = True)
    pdf.set_xy(95 + 2 * d_cell_b, 16.5 + d_cell_h)
    pdf.cell(d_cell_b, d_cell_h , txt = name_date, border = 1, ln = 0, align = 'R', fill = True)

    pdf.set_font('Helvetica', '', 8)
    pdf.set_xy(95 + d_cell_b, 16.5 - d_cell_h)
    pdf.cell(d_cell_b, d_cell_h , txt = form_data['obra'], border = 'TB', ln = 0, align = 'R', fill = False)
    pdf.set_xy(95 + 3 * d_cell_b, 16.5 - d_cell_h)
    pdf.cell(d_cell_b, d_cell_h , txt = form_data['muestra'], border = 'TB', ln = 0, align = 'R', fill = False)
    pdf.set_xy(95 + d_cell_b, 16.5)
    pdf.cell(d_cell_b, d_cell_h , txt = form_data['localizacion'], border = 'TB', ln = 0, align = 'R', fill = False)
    pdf.set_xy(95 + d_cell_b, 16.5 + d_cell_h)
    pdf.cell(d_cell_b, d_cell_h , txt = form_data['profundidad'], border = 'B', ln = 0, align = 'R', fill = False)
    pdf.set_xy(95 + 3 * d_cell_b, 16.5)
    pdf.cell(d_cell_b, d_cell_h , txt = form_data['elaboro'], border = 'TB', ln = 0, align = 'R', fill = False)
    pdf.set_xy(95 + 3 * d_cell_b, 16.5 + d_cell_h)
    pdf.cell(d_cell_b, d_cell_h , txt = form_data['fecha'], border = 'B', ln = 0, align = 'R', fill = False)

    pdf.image('fack1.png', x = 10, y = 180, w = 20, h = 20, type = 'PNG')
    pdf.image('fack2.png', x = 30 + 5 , y = 180, w = 20, h = 20, type = 'PNG')
    pdf.image('fack3.png', x = 50 + 10 , y = 180, w = 20, h = 20, type = 'PNG')

    pdf.set_font('Helvetica', '', 9)
    pdf.set_xy(10, 16.5 + d_cell_h * 3)
    pdf.cell(d_cell_b / 2, d_cell_h, txt = name_mesh, border = 1, ln = 0,align = 'C', fill = True, link = '')
    pdf.set_xy(10 + d_cell_b / 2, 16.5 + d_cell_h * 3)
    pdf.cell(10 + d_cell_b / 3, d_cell_h, txt = name_wret, border = 1, ln = 0,align = 'C', fill = True, link = '')
    pdf.set_xy((10 + d_cell_b /2) + 10 + d_cell_b / 3 , 16.5 + d_cell_h * 3)
    pdf.cell(5 + (10 + d_cell_b / 2)/2, d_cell_h, txt = name_passes, border = 1, ln = 0,align = 'C', fill = True, link = '')

    amount = len(datos['mesh'])
    for i in range(amount):
      height = 130 / amount
      pdf.set_xy(10, 42.95833333 + height * i)
      pdf.cell(d_cell_b / 2, height, txt = datos['mesh_name'][i], border = 1, ln = 0,align = 'C', fill = False)
      pdf.set_xy(10 + d_cell_b / 2, 42.95833333 + height * i)
      pdf.cell(10 + d_cell_b / 3, height, txt = str(datos['peso_ret'][i]), border = 1, ln = 0,align = 'C', fill = False)
      pdf.set_xy((10 + d_cell_b /2) + 10 + d_cell_b / 3 , 42.95833333 + height * i)
      pdf.cell(5 + (10 + d_cell_b / 2)/2, height, txt = str(round(datos['passing'][i], 2)), border = 1, ln = 0,align = 'C', fill = False)

    pdf.image('fig_sieve.png', x = 85, y = 35, w = 190, h = 120, type = 'PNG')
    pdf.set_xy(100, 160)
    pdf.cell(55, 8 , txt = name_gravel +": "+ str(round(datos['gravel'], 2)) + " %", border = 1, ln = 0, align = 'C', fill = False)
    pdf.set_xy(100+55, 160)
    pdf.cell(75, 8 , txt = name_sand +": "+ str(round(datos['sand'], 2)) + " %", border = 1, ln = 0, align = 'C', fill = False)
    pdf.set_xy(100+55+75, 160)
    pdf.cell(36.225, 8 , txt = name_fines +": "+ str(round(datos['fines'], 2)) + " %", border = 1, ln = 0, align = 'C', fill = False)

    b , h = 20, d_cell_h
    x, y = 100, 170
    pdf.set_xy(x, y)
    pdf.cell(b, h , txt = 'D60', border = 1, ln = 0, align = 'C', fill = True)
    pdf.set_xy(x, y+h)
    pdf.cell(b, h , txt = 'D30', border = 1, ln = 0, align = 'C', fill = True)
    pdf.set_xy(x, y+h+h)
    pdf.cell(b, h , txt = 'D10', border = 1, ln = 0, align = 'C', fill = True)
    if type(datos['d60']) != type(str("sda")):
      pdf.set_xy(x+b, y)
      pdf.cell(b, h , txt = str(round(datos['d60'], 3)), border = 1, ln = 0, align = 'C', fill = False)
      pdf.set_xy(x+b, y+h)
      pdf.cell(b, h , txt = str(round(datos['d30'], 3)), border = 1, ln = 0, align = 'C', fill = False)
      pdf.set_xy(x+b, y+h+h)
      pdf.cell(b, h , txt = str(round(datos['d10'], 3)), border = 1, ln = 0, align = 'C', fill = False)
    else:
      pdf.set_xy(x+b, y)
      pdf.cell(b, h , txt = "--", border = 1, ln = 0, align = 'C', fill = False)
      pdf.set_xy(x+b, y+h)
      pdf.cell(b, h , txt = "--", border = 1, ln = 0, align = 'C', fill = False)
      pdf.set_xy(x+b, y+h+h)
      pdf.cell(b, h , txt = "--", border = 1, ln = 0, align = 'C', fill = False)
    x, y = 155, 170
    pdf.set_xy(x, y)
    pdf.cell(b, h , txt = 'CU', border = 1, ln = 0, align = 'C', fill = True)
    pdf.set_xy(x, y+h)
    pdf.cell(b, h , txt = 'CC', border = 1, ln = 0, align = 'C', fill = True)
    pdf.set_xy(x, y+h+h)
    pdf.cell(b, h , txt = 'SUCS', border = 1, ln = 0, align = 'C', fill = True)
    if type(datos['d60']) != type(str("sda")):
      pdf.set_xy(x+b, y)
      pdf.cell(b, h , txt = str(round(datos['cu'], 3)), border = 1, ln = 0, align = 'C', fill = False)
      pdf.set_xy(x+b, y+h)
      pdf.cell(b, h , txt = str(round(datos['cc'], 3)), border = 1, ln = 0, align = 'C', fill = False)
    else:
      pdf.set_xy(x+b, y)
      pdf.cell(b, h , txt = "--", border = 1, ln = 0, align = 'C', fill = False)
      pdf.set_xy(x+b, y+h)
      pdf.cell(b, h , txt = "--", border = 1, ln = 0, align = 'C', fill = False)
    pdf.set_xy(x+b, y+h+h)
    pdf.cell(b, h , txt = datos['sucs'], border = 1, ln = 0, align = 'C', fill = False)
    pdf.set_xy(86, 105)
    pdf.rotate(90)
    pdf.set_font('Helvetica', '', 10)
    pdf.cell(b, h , txt = name_passes, border = 0, ln = 0, align = 'C', fill = False)
    pdf.rotate(0)
    pdf.set_xy(180, 150)
    pdf.cell(b, h , txt = name_xaxis, border = 0, ln = 0, align = 'C', fill = False)
    pdf.output('sieve.pdf', 'F')
    import os
    os.system("sieve.pdf")

  def Plast_PDF(self, form_data, datos_pl, yu):
      from fpdf import FPDF
      import fpdf

      global languages
      sentences = languages[yu]
      f = 0
      name_obra = sentences[f][1]
      name_location = sentences[f][2]
      name_depth = sentences[f][3]
      name_sample = sentences[f][4]
      name_author = sentences[f][5]
      name_date = sentences[f][6]
      name_xaxis2 = sentences[f][14]
      name_titulo2 = sentences[f][15]

      name_hits = sentences[f][16]
      name_id = sentences[f][17]
      name_wr = sentences[f][18]
      name_wrw = sentences[f][19]
      name_wrs = sentences[f][20]
      name_ww = sentences[f][21]
      name_ws = sentences[f][22]
      name_wcont = sentences[f][23]
      name_ll = sentences[f][24]
      name_pl = sentences[f][25]

      pdf = FPDF(orientation = 'P', unit = 'mm', format=(297,210))
      pdf.add_page(orientation = 'L')
      pdf.set_font('Helvetica', '', 12)
      pdf.set_fill_color(217, 217, 217)
      d_cell_h, d_cell_b = 6.6145833325, 42.333333328
      b , h = 20, d_cell_h
      pdf.set_xy(10, 16.5 - d_cell_h)
      pdf.cell(190, d_cell_h * 3 , txt = name_titulo2, border = 1, ln = 0, align = 'C', fill = True)
      pdf.set_xy(10, 16.5 + d_cell_h* 2)
      pdf.cell(d_cell_b, d_cell_h , txt = name_obra, border = 1, ln = 0, align = 'R', fill = True)
      pdf.set_xy(10, 16.5 + d_cell_h *3)
      pdf.cell(d_cell_b, d_cell_h , txt = name_location, border = 1, ln = 0, align = 'R', fill = True)
      pdf.set_xy(10, 16.5 + d_cell_h *4)
      pdf.cell(d_cell_b, d_cell_h , txt = name_depth, border = 1, ln = 0, align = 'R', fill = True)

      pdf.set_xy(100, 16.5 + d_cell_h *2)
      pdf.cell(d_cell_b, d_cell_h , txt = name_sample, border = 1, ln = 0, align = 'R', fill = True)
      pdf.set_xy(100, 16.5 + d_cell_h *3)
      pdf.cell(d_cell_b, d_cell_h , txt = name_author, border = 1, ln = 0, align = 'R', fill = True)
      pdf.set_xy(100, 16.5 + d_cell_h *4)
      pdf.cell(d_cell_b, d_cell_h , txt = name_date, border = 1, ln = 0, align = 'R', fill = True)

      pdf.set_font('Helvetica', '', 8)
      pdf.set_xy(10+d_cell_b, 16.5 + d_cell_h *2)
      pdf.cell((190/2) - d_cell_b-5, d_cell_h , txt = form_data['obra'], border = 1, ln = 0, align = 'R', fill = False)
      pdf.set_xy(10+d_cell_b, 16.5 + d_cell_h *3)
      pdf.cell((190/2) - d_cell_b-5, d_cell_h , txt = form_data['localizacion'], border = 1, ln = 0, align = 'R', fill = False)
      pdf.set_xy(10+d_cell_b, 16.5 + d_cell_h *4)
      pdf.cell((190/2) - d_cell_b-5, d_cell_h , txt = form_data['profundidad'], border = 1, ln = 0, align = 'R', fill = False)

      pdf.set_xy(d_cell_b+(190/2)+5, 16.5 + d_cell_h *2)
      pdf.cell((190/2) - d_cell_b+5, d_cell_h , txt = form_data['muestra'], border = 1, ln = 0, align = 'R', fill = False)
      pdf.set_xy(d_cell_b+(190/2)+5, 16.5 + d_cell_h *3)
      pdf.cell((190/2) - d_cell_b+5, d_cell_h , txt = form_data['elaboro'], border = 1, ln = 0, align = 'R', fill = False)
      pdf.set_xy(d_cell_b+(190/2)+5, 16.5 + d_cell_h *4)
      pdf.cell((190/2) - d_cell_b+5, d_cell_h , txt = form_data['fecha'], border = 1, ln = 0, align = 'R', fill = False)

      pdf.set_font('Helvetica', '', 12)
      pdf.image('fig_plast.png', x = 160, y = 200, w = 40, h = 30, type = 'PNG')
      pdf.image('fig_hits.png', x = 20, y = 150, w = 140, h = 110, type = 'PNG')
      pdf.set_xy(80, 258)
      pdf.cell(b, h , txt = name_xaxis2, border = 0, ln = 0, align = 'C', fill = False)

      b = 20
      pdf.set_xy(30, 56)
      pdf.cell(b*8, 6 , txt = name_ll, border = 1, ln = 0, align = 'L', fill = True)
      pdf.set_xy(30, 62)
      pdf.cell(b, h , txt = name_hits, border = 1, ln = 0, align = 'C', fill = True)
      pdf.set_xy(30+ b, 62)
      pdf.cell(b, h, txt = name_id, border = 1, ln = 0, align = 'C', fill = True)
      pdf.set_xy(30+ b*2, 62)
      pdf.cell(b, h, txt = name_wr, border = 1, ln = 0, align = 'C', fill = True)
      pdf.set_xy(30+ b*3, 62)
      pdf.cell(b, h, txt = name_wrw, border = 1, ln = 0, align = 'C', fill = True)
      pdf.set_xy(30+ b*4, 62)
      pdf.cell(b, h, txt = name_wrs, border = 1, ln = 0, align = 'C', fill = True)
      pdf.set_xy(30+ b*5, 62)
      pdf.cell(b, h, txt = name_ww, border = 1, ln = 0, align = 'C', fill = True)
      pdf.set_xy(30+ b*6, 62)
      pdf.cell(b, h, txt = name_ws, border = 1, ln = 0, align = 'C', fill = True)
      pdf.set_xy(30+ b*7, 62)
      pdf.cell(b, h, txt = name_wcont, border = 1, ln = 0, align = 'C', fill = True)

      for i, j in enumerate(datos_pl['lld']):
        i += 1
        pdf.set_xy(30, 62+ h * i)
        pdf.cell(b, h , txt = str(round(j[0],2)), border = 1, ln = 0, align = 'C', fill = False)
        pdf.set_xy(30+ b, 62+ h * i)
        pdf.cell(b, h, txt = j[1], border = 1, ln = 0, align = 'C', fill = False)
        pdf.set_xy(30+ b*2, 62+ h * i)
        pdf.cell(b, h, txt = str(round(j[2],2)), border = 1, ln = 0, align = 'C', fill = False)
        pdf.set_xy(30+ b*3, 62+ h * i)
        pdf.cell(b, h, txt = str(round(j[3],2)), border = 1, ln = 0, align = 'C', fill = False)
        pdf.set_xy(30+ b*4, 62+ h * i)
        pdf.cell(b, h, txt = str(round(j[4],2)), border = 1, ln = 0, align = 'C', fill = False)
        pdf.set_xy(30+ b*5, 62+ h * i)
        pdf.cell(b, h, txt = str(round(j[5],2)), border = 1, ln = 0, align = 'C', fill = False)
        pdf.set_xy(30+ b*6, 62+ h * i)
        pdf.cell(b, h, txt = str(round(j[6],2)), border = 1, ln = 0, align = 'C', fill = False)
        pdf.set_xy(30+ b*7, 62+ h * i)
        pdf.cell(b, h, txt = str(round(j[7],2)), border = 1, ln = 0, align = 'C', fill = False)

      y = pdf.get_y()
      pdf.set_xy(30, y+h)
      pdf.cell(b*8, h , txt = name_pl, border = 1, ln = 0, align = 'L', fill = True)
      y = pdf.get_y()
      pdf.set_xy(30, y+h)
      for i, j in enumerate(datos_pl['pld']):
        i += 1
        pdf.set_xy(30, y + h * i)
        pdf.cell(b, h , txt = "", border = 1, ln = 0, align = 'C', fill = False)
        pdf.set_xy(30+ b, y + h * i)
        pdf.cell(b, h, txt = j[0], border = 1, ln = 0, align = 'C', fill = False)
        pdf.set_xy(30+ b*2, y + h * i)
        pdf.cell(b, h, txt = str(round(j[1],2)), border = 1, ln = 0, align = 'C', fill = False)
        pdf.set_xy(30+ b*3, y + h * i)
        pdf.cell(b, h, txt = str(round(j[2],2)), border = 1, ln = 0, align = 'C', fill = False)
        pdf.set_xy(30+ b*4, y + h * i)
        pdf.cell(b, h, txt = str(round(j[3],2)), border = 1, ln = 0, align = 'C', fill = False)
        pdf.set_xy(30+ b*5, y + h * i)
        pdf.cell(b, h, txt = str(round(j[4],2)), border = 1, ln = 0, align = 'C', fill = False)
        pdf.set_xy(30+ b*6, y + h * i)
        pdf.cell(b, h, txt = str(round(j[5],2)), border = 1, ln = 0, align = 'C', fill = False)
        pdf.set_xy(30+ b*7, y + h * i)
        pdf.cell(b, h, txt = str(round(j[6],2)), border = 1, ln = 0, align = 'C', fill = False)

      pdf.set_xy(210-10-2*b, 2.5+150)
      pdf.cell(b, h, txt = "LL", border = 1, ln = 0, align = 'R', fill = True)
      pdf.set_xy(210-10-2*b, 2.5+150+h)
      pdf.cell(b, h, txt = "PL", border = 1, ln = 0, align = 'R', fill = True)
      pdf.set_xy(210-10-2*b, 2.5+150+h*2)
      pdf.cell(b, h, txt = "Fw", border = 1, ln = 0, align = 'R', fill = True)
      pdf.set_xy(210-10-2*b, 2.5+150+h*3)
      pdf.cell(b, h, txt = "Ip", border = 1, ln = 0, align = 'R', fill = True)
      pdf.set_xy(210-10-2*b, 2.5+150+h*4)
      pdf.cell(b, h, txt = "IpA", border = 1, ln = 0, align = 'R', fill = True)
      pdf.set_xy(210-10-2*b, 2.5+150+h*5)
      pdf.cell(b, h, txt = "USCS", border = 1, ln = 0, align = 'R', fill = True)

      pdf.set_xy(210-10-b, 2.5+150)
      pdf.cell(b, h, txt = str(round(datos_pl["ll"], 2)), border = 1, ln = 0, align = 'C', fill = False)
      pdf.set_xy(210-10-b, 2.5+150+h)
      pdf.cell(b, h, txt = str(round(datos_pl["pl"], 2)), border = 1, ln = 0, align = 'C', fill = False)
      pdf.set_xy(210-10-b, 2.5+150+h*2)
      pdf.cell(b, h, txt = str(round(datos_pl["Fw"], 2)), border = 1, ln = 0, align = 'C', fill = False)
      pdf.set_xy(210-10-b, 2.5+150+h*3)
      pdf.cell(b, h, txt = str(round(datos_pl["Ip"], 2)), border = 1, ln = 0, align = 'C', fill = False)
      pdf.set_xy(210-10-b, 2.5+150+h*4)
      pdf.cell(b, h, txt = str(round(datos_pl["IpA"], 2)), border = 1, ln = 0, align = 'C', fill = False)
      pdf.set_xy(210-10-b, 2.5+150+h*5)
      pdf.cell(b, h, txt = str(datos_pl["sucs"]), border = 1, ln = 0, align = 'C', fill = False)

      pdf.image('fack1.png', x = 10, y = 267, w = 20, h = 20, type = 'PNG')
      pdf.image('fack2.png', x = 30 + 5 , y = 267, w = 20, h = 20, type = 'PNG')
      pdf.image('fack3.png', x = 50 + 10 , y = 267, w = 20, h = 20, type = 'PNG')

      pdf.output('plast.pdf', 'F')
      import os
      os.system("plast.pdf")
      