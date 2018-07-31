#!/usr/bin/python
# -*- coding: UTF-8 -*-
# zip -q -r -e -m -o [yourName].zip someThing
import os
import subprocess
import time
import uuid
from os.path import dirname, abspath
from . import ZipUtilities
from spring.models import ProjectInfo

from jinja2 import PackageLoader, Environment

ROOT = abspath(dirname(__file__))
env = Environment(loader=PackageLoader(os.path.split(ROOT)[-1], 'templates'))

demoPath = ROOT + "/templates/"
demoPro = "{module}"
cuModuleName = "jingxuan"
cuProjectName = "log"


def first_upper(name):
    return name[0].capitalize() + name[1:]


config = {
    "module": cuModuleName,
    "Module": first_upper(cuModuleName),
    "project": cuProjectName,
    "module_project": cuModuleName + "-" + cuProjectName,
    "ModuleProject": first_upper(cuModuleName) + first_upper(cuProjectName),

}


def copy_pro(module_name="module"):
    return "cd {0} && rm -rf {2}* && cp -R  {1} {2}".format(demoPath, demoPro, module_name)


def zip_file(module_name="module"):
    return "zip -q -r {0}.zip {0}".format(module_name)


def remove_file(file=''):
    return "rm -rf {0}".format(file)


def rename(path):
    for moduleDir in os.listdir(path):
        os.chdir(path)
        path_name = moduleDir.replace("{module}", cuModuleName).replace("{project}", cuProjectName) \
            .replace("{ModuleProject}", config.get("ModuleProject"))
        if "{module}" in moduleDir or "{project}" in moduleDir:
            os.rename(moduleDir, path_name)
        if os.path.isdir(os.path.join(path, path_name)):
            rename(path + "/" + path_name)
        else:
            if moduleDir.endswith("tpl"):
                tpl_path = os.path.join(path, moduleDir).replace(demoPath, "")
                template = env.get_template(tpl_path)
                html = template.render(config)
                save_dir = os.path.join(path, moduleDir). \
                    replace(".tpl", "").replace("{Module}", config.get("Module")) \
                    .replace("{ModuleProject}", config.get("ModuleProject"))
                with open(save_dir, "wb+") as fp:
                    fp.write(html.encode("utf-8"))
                os.remove(os.path.join(path, moduleDir))


def gen_tpl(module_name, project_name):
    global cuModuleName
    cuModuleName = module_name
    global cuProjectName
    cuProjectName = project_name
    subprocess.Popen(copy_pro(cuModuleName + "-" + cuProjectName), stderr=subprocess.PIPE,
                     stdout=subprocess.PIPE, shell=True)
    time.sleep(0.5)
    rename(demoPath + cuModuleName + "-" + cuProjectName)
    project_id = uuid.uuid4()
    ProjectInfo.objects.create(projectId=project_id,
                               projectName=(cuModuleName + "-" + cuProjectName),
                               location=demoPath)
    return project_id


def get(project_id: object) -> object:
    project_info = ProjectInfo.objects.get(projectId=project_id)
    project_path = project_info.location
    project_name = project_info.projectName
    os.chdir(project_path)
    utilities = ZipUtilities.ZipUtilities()
    tmp_dl_path = os.path.join(project_path, project_name)
    utilities.toZip(tmp_dl_path, project_name)
    # subprocess.Popen(zip_file(cuModuleName + "-" + cuProjectName),
    #                  stderr=subprocess.PIPE, stdout=subprocess.PIPE, shell=True)
    # subprocess.Popen(remove_file(cuModuleName + "-" + cuProjectName), stderr=subprocess.PIPE,
    #                  stdout=subprocess.PIPE, shell=True)
    return {
        "zip_file": utilities.zip_file,
        "zip_name": project_name+".zip"
    }
