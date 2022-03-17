from jinja2 import Environment, FileSystemLoader
import sys
import json


def generate_html(json_data):
    env = Environment(loader=FileSystemLoader('./'))
    template = env.get_template('template.html')
    output_file = json_data['output']+'result.html'
    with open(output_file, 'w+', encoding="utf-8") as fout:
        html_content = template.render(json_data=json_data)
        fout.write(html_content)
        print('输出文件:'+output_file)


if __name__ == '__main__':
    try:
        json_path = sys.argv[1]
    except BaseException:
        print('Error: 读取json文件失败，请检查')
    else:
        with open(json_path, 'r', encoding='utf8')as fp:
            json_data = json.load(fp)
            print('json数据:', json_data)
            try:
                output = json_data['output']
            except BaseException:
                print('未配置"output"输出路径,请检查')
            else:
                generate_html(json_data)
