
import openpyxl
from PIL import Image, ImageDraw, ImageFont

workbooks_alunos = openpyxl.load_workbook('planilha_alunos.xlsx')
sheet_alunos = workbooks_alunos['Sheet1']

for indice, linha in enumerate(sheet_alunos.iter_rows(min_row=2, max_row=2)):
    nome_curso = linha[0].value
    nome_participante = linha[1].value
    tipo_participante = linha[2].value
    data_inicio = linha[3].value
    data_final = linha[4].value
    carga_horaria = linha[5].value
    data_emissao = linha[6].value

    font_nome = ImageFont.truetype('/Users/rafaelbatista/PycharmProjects/Arial Bold.ttf', 90)
    font_geral = ImageFont.truetype('/Users/rafaelbatista/PycharmProjects/Arial.ttf', 80)
    font_data = ImageFont.truetype('/Users/rafaelbatista/PycharmProjects/Arial.ttf', 55)

    image = Image.open('/Users/rafaelbatista/PycharmProjects/automacao-certificado/certificado_padrao.jpg')
    desenhar = ImageDraw.Draw(image)

    desenhar.text((1020, 827), nome_participante, fill='black', font=font_nome)
    desenhar.text((1060, 950), nome_curso, fill='black', font=font_geral)
    desenhar.text((1435, 1065), tipo_participante, fill='black', font=font_geral)
    desenhar.text((1480, 1182), str(carga_horaria), fill='black', font=font_geral)

    desenhar.text((750, 1770), str(data_inicio), fill='black', font=font_data)
    desenhar.text((750, 1930), str(data_final), fill='black', font=font_data)

    desenhar.text((2220, 1930), str(data_emissao), fill='black', font=font_data)

    image.save(f'/Users/rafaelbatista/PycharmProjects/automacao-certificado/{indice} {nome_participante} certificado.jpg')
