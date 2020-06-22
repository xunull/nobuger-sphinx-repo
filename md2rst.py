
import os
import subprocess
from git import Repo

repo_path = os.path.dirname(os.path.abspath(__file__))
blog_path = os.path.join(repo_path, 'source')


def git_check():
    repo = Repo.init(path=repo_path)
    if not repo.is_dirty():
        exit(0)


def get_md_dir():
    res = []
    fs = os.listdir(blog_path)
    for f in fs:
        if f.startswith('md-'):
            abs_path = os.path.join(blog_path, f)
            res.append(abs_path)
    return res


def md5_to_rst(file):
    filename, ext = os.path.splitext(file)
    convert_cmd = 'pandoc -f markdown -t rst {md_file} -o {rst_file}'.format(
        md_file=filename+'.md', rst_file=filename+'.rst'
    )
    status = subprocess.call(convert_cmd.split(" "))
    if status != 0:
        print("执行失败: " + convert_cmd)
        os._exit(1)
    if status == 0:
        print(file + ' 处理完成')
    else:
        print(file + '处理失败')


def main():
    for folder in get_md_dir():
        # 每个类别下面的章节目录
        print(folder)
        target_dir = os.listdir(folder)
        for one in target_dir:
            print(one)
            abs_path = os.path.join(folder, one)
            os.chdir(abs_path)
            fs = os.listdir(abs_path)
            md_files = sorted([file for file in fs if file.endswith('md')])

            for file in md_files:
                md5_to_rst(file)


if __name__ == '__main__':
    main()
    print('over')
