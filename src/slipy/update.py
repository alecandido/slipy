import pathlib

from . import utils


def update(folder):
    project_dir = pathlib.Path(folder)
    assets_dir = project_dir / ".presentation"

    presentation_cfg = utils.load_cfg(project_dir)
    update_template(assets_dir, presentation_cfg)
    update_theme(assets_dir, presentation_cfg)


def update_template(assets_dir, presentation_cfg):
    framework = presentation_cfg["framework"]
    name = presentation_cfg["template"]["name"]

    utils.switch_framework(framework).assets.update_template(name, assets_dir)


def update_theme(assets_dir, presentation_cfg):
    framework = presentation_cfg["framework"]
    name = presentation_cfg["theme"]["name"]

    utils.switch_framework(framework).assets.update_theme(name, assets_dir)