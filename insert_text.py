import xml.etree.ElementTree as ET
name = 'text_ui_quest.xml'
pin = './example'
pout = './example/ready_for_pack'
fin = f'{pin}/{name}'
fout = f'{pout}/{name}'
tree = ET.parse(fin)
root = tree.getroot()
for row in root.findall('Row'):
    cells = row.findall('Cell')
    if len(cells) == 3: 
        id_cell = cells[0].text  # ID
        english_text = cells[1].text  # ENGLISH
        chinese_text = cells[2].text  # LOCAL_LANGUAGE

        #CUSTOM RULES
        #FOR UI_ITEMS.XML
        c = "\\n"
        if id_cell.startswith('ui_nm'):
            c = ''
        #FOR UI_SOUL.XML
        #
        #

        combined_text = f"{chinese_text} {c} {english_text}"
        cells[2].text = combined_text
tree.write(fout, encoding='utf-8', xml_declaration=True)