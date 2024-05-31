import codecs
import logging

def updateSvg(template_svg_filename,output_dict,output_svg_filename):
    print(f"updateSvg called with {output_dict} and {template_svg_filename}")
    output = codecs.open(template_svg_filename, 'r', encoding='utf-8').read()
    for output_key in output_dict:
        output = output.replace(output_key, output_dict[output_key])
    # todo: write generated file to pic/icons instead of src
    codecs.open(output_svg_filename, 'w', encoding='utf-8').write(output)