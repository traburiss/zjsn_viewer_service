from django.db import models

# Create your models here.


BEFORE_STATIC_URL = "http://192.168.31.207:8000/"


class KanmusuEquipment(models.Model):
    # 图鉴编号
    equipment_id = models.TextField()
    # 装备名
    equipment_name = models.TextField()
    # 稀有度
    equipment_level = models.TextField()
    # 装备类型
    equipment_type = models.TextField()
    # 适用船类型
    equipment_suit_type = models.TextField()
    # 来源
    equipment_from = models.TextField()
    # 开发时间
    equipment_make_time = models.TextField()
    # 开发阈值
    equipment_make_threshold = models.TextField()
    # 废弃
    equipment_discard = models.TextField()
    # 射程
    equipment_range = models.TextField()
    # 火力
    equipment_fire = models.TextField(default='0')
    # 鱼雷
    equipment_torpedo = models.TextField(default='0')
    # 对潜
    equipment_antisubmarine = models.TextField(default='0')
    # 轰炸
    equipment_boom = models.TextField(default='0')
    # 对空
    equipment_antiair = models.TextField(default='0')
    # 装甲
    equipment_armor = models.TextField(default='0')
    # 命中
    equipment_hit = models.TextField(default='0')
    # 回避
    equipment_flee = models.TextField(default='0')
    # 索敌
    equipment_tracking = models.TextField(default='0')
    # 幸运
    equipment_lucky = models.TextField(default='0')
    # 对空补正
    equipment_antiair_correct = models.TextField(default='0')
    # 特殊效果
    equipment_special_effect = models.TextField()
    # 说明
    equipment_info = models.TextField()
    # 图片地址
    equipment_pic = models.TextField()

    def to_dict(self):
        return {
            'equipment_id': self.equipment_id,
            'equipment_name': self.equipment_name,
            'equipment_level': self.equipment_level,
            'equipment_type': self.equipment_type,
            'equipment_suit_type': self.equipment_suit_type,
            'equipment_from': self.equipment_from,
            'equipment_make_time': self.equipment_make_time,
            'equipment_make_threshold': self.equipment_make_threshold,
            'equipment_discard': self.equipment_discard,
            'equipment_range': self.equipment_range,
            'equipment_fire': self.equipment_fire,
            'equipment_torpedo': self.equipment_torpedo,
            'equipment_antisubmarine': self.equipment_antisubmarine,
            'equipment_boom': self.equipment_boom,
            'equipment_antiair': self.equipment_antiair,
            'equipment_armor': self.equipment_armor,
            'equipment_hit': self.equipment_hit,
            'equipment_flee': self.equipment_flee,
            'equipment_tracking': self.equipment_tracking,
            'equipment_lucky': self.equipment_lucky,
            'equipment_antiair_correct': self.equipment_antiair_correct,
            'equipment_special_effect': self.equipment_special_effect,
            'equipment_info': self.equipment_info,
            'equipment_pic': BEFORE_STATIC_URL + self.equipment_pic,
        }










