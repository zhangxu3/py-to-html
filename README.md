## 运行脚本

### Author: zhangxu3@genomics.cn 🚀

```bash
# 下载
git clone https://github.com/zhangxu3/py-to-html.git

# 进入目录
cd py-to-html

# 安装依赖
pip install jinja2

# 运行，读取的json文件路径（测试用）
py html.py ./test/test.json
```

```bash
// 👉 json 结构和字段
{
  "title": "**", // 报告标题
  "output":"", // html输出路径
  "data":[
    {
      "path":"", // svg/png路径
      "description":"" // 图片描述
    }
    // ...
  ]
}
```
