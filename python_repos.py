import requests
import pygal
from pygal.style import LightColorizedStyle as LCS,LightenStyle as LS
#执行API调用并存储响应
url='https://api.github.com/search/repositories?q=language:python&sort=stars'
r=requests.get(url)
print("状态码:",r.status_code)

# 将API响应存储在一个变量中
response_dict=r.json()
print("全部仓库:",response_dict['total_count'])
# # 处理结果
# print(response_dict.keys())
# 搜索有关仓库的信息
repo_dicts=response_dict['items']
print("项目数",len(repo_dicts))
# 研究第一个仓库
# repo_dict=repo_dicts[0]
# print("\nKeys：",len(repo_dict))
# for key in sorted(repo_dict.keys()):
#     print(key)

# print("\n---仓库的部分信息---")
# for repo_dict in repo_dicts:
#     print('名称：',repo_dict['name'])
#     print('作者：',repo_dict['owner']['login'])
#     print('点星：',repo_dict['stargazers_count'])
#     print('仓库：',repo_dict['html_url'])
#     # print('创建：',repo_dict['created_at'])
#     # print('更新：',repo_dict['updated_at'])
#     print('描述：',repo_dict['description'])
#可视化
# names,stars=[],[]
names,plot_dicts=[],[]
for repo_dict in repo_dicts:
    names.append(repo_dict['name'])
    # stars.append(repo_dict['stargazers_count'])
    plot_dict={
        'value':repo_dict['stargazers_count'],
        'label':str(repo_dict['description']),
        'xlink':repo_dict['html_url'],
    }
    plot_dicts.append(plot_dict)
my_style=LS('#333366',base_style=LCS)
# 图表样式定制
my_config=pygal.Config()
my_config.x_label_rotation=45
my_config.show_legend=False
my_config.title_font_size=24
my_config.label_font_size=14
my_config.major_label_font_size=18
my_config.truncate_label=15
my_config.show_y_guides=False
my_config.width=1000

chart=pygal.Bar(my_config,style=my_style)
chart.title="Github上获得最多Stars的Python项目"
chart.x_labels=names

chart.add('',plot_dicts)
chart.render_to_file('python_ropes.svg')

with open('index.html','w',encoding='utf-8') as html_file:
    html_file.write('<html><head><title>Github上获得最多Stars的Python项目</title><meta charset="utf-8"></head><body><h1>Github上获得最多Stars的Python项目</h1>\n')
    for svg in['python_ropes.svg']:
        html_file.write('  <object type="image/svg+xml" data="{0}" height=500></object>\n'.format(svg))
        html_file.write('</body></html>')