from util import *

def get_all_collection_name()->list:
    ita = load_json("itemall.json", "assests")
    ret_list=[]
    i=0
    for feature in ita:
        i+=1
        if feature == None:
            continue
        for item in feature["features"]:
            ret_list.append(item["properties"]["popTitle"])
    # print()
    black_list = ['狂风，听谁号令', '听海人', '手鞠游戏', '突发委托', '相位之门', '石碑', '键纹基座Ⅰ']
    '松茸 - 蒙德'
    '甜甜花 - 蒙德'
    '树莓 - 蒙德'
    '盗宝团 - 蒙德'
    '宝箱 - 蒙德'
    '丘丘人 - 蒙德'
    '薄荷 - 蒙德'
    '蝴蝶翅膀 - 蒙德'
    '鸟蛋 - 蒙德'
    '冷鲜肉 - 蒙德'
    '晶核 - 蒙德'
    '螃蟹 - 蒙德'
    '白萝卜 - 蒙德'
    '松果 - 蒙德'
    '遗迹守卫 - 蒙德'
    '风晶蝶 - 蒙德'
    
    
    """全列表如下：(version: v0.3.0.331)

    ['突发委托', '雷神瞳2', '兽肉 - 稻妻', '相位之门', '石碑', '深海龙蜥 - 渊下宫', '键纹基座Ⅰ', '禽肉 - 稻妻', '史莱姆 - 蒙德', '雪山迷踪
', , '摩拉调查点 - 稻妻', '武器调查点 - 鹤观', '愚人众先遣队 - 璃月', '【「清籁岛」的记录画片 · 之二】对应拍照点', '史莱姆 - 鹤观', '盗宝团 - 璃月', '发光髓-群岛', '「无名小岛」的壁画', '止水之潘', '深渊法师 - 稻妻', '天遒宝迹', '水晶矿 - 群岛', '传送锚点 - 稻妻 - 鹤观', '海上拾玉', '雾海纪行 - 要求特别多的作家', '苹果 - 稻妻', '史莱姆 - 群 
岛', '冒险家协会的诸多事宜', '键纹基座Ⅱ', '灵钜有宝予何人', '魔晶矿 - 璃月', '甜甜花 - 鹤观', '螃蟹 - 鹤观', '遗迹机兵 - 稻妻', '厄瑞玻斯的秘密 - 八衢姬之试炼', '古老的石板', '玄
月宝箱 - 璃月', '禽肉 - 稻妻2', '雾海纪行 - 雾海与树之祭', '鸟蛋 - 鹤观', '钓鱼点 - 渊下宫', '鳗肉 - 稻妻', '畅畅和他的小伙伴', 'NPC奖励 - 璃月', '食谱 - 稻妻2', '飘浮灵 - 渊下宫
', '限时挑战', '铭记之谷', '矿物调查点 - 稻妻', '传送锚点 - 璃月 - 珉林', '突发委托-璃月', '铁矿 - 群岛', '永无止境的研究', '老婆婆【宇奈】 - 鹤观', '孤独的海兽', '震雷连山密宫「
炼武秘境：鸣雷城墟」', '樱树 - 梦见木 - 稻妻', '传送点 - 稻妻 - 八酝岛', '食谱 - 璃月', '鸟蛋 - 稻妻2', '遗迹人形 - 鹤观', '时与风', '【寝子是只猫】系列', '青蛙 - 蒙德', '钓鱼与 
护身符 【伊部】', '等量交换', , '骗骗花 - 海岛', '木匣 - 稻妻', '螃蟹 - 璃月', '遗迹机兵 - 鹤观', '工作迫近', '圣遗物调查点 - 稻妻2', '地理志-蒙德', '电气水晶-群岛
', '此诗送此城', '雪山大勘探', '胡萝卜 - 稻妻', , '旧味难寻', '低温调查', '传送锚点 - 璃月 - 云来海', '兽肉 - 海岛', '堇瓜 - 稻妻', '妖狸 - 稻妻', 'NPC商店 - 蒙德', 
'大生意', '水泡泡', , '塞西莉亚苗圃', '紫晶矿 - 稻妻', '白萝卜-群岛', '夜叉之愿', '砂流之庭', '清籁旧宝', '书籍 - 稻妻2', '蝴蝶翅膀 - 稻妻2', '【第一章 第四幕 · 报幕
】戴因斯雷布', '门户清理', , , '藏宝图【岻伽】', '酒庄大扫除', '薄荷 - 璃月', '传送锚点 - 蒙德 - 明冠山地', '铁矿 - 鹤观', '收集风之印的少女', '甜甜花 - 稻
妻', '鸣草 - 稻妻', '公主之匣', '遗迹机兵 - 渊下宫', , '深入风龙废墟', '大型丘丘人 - 璃月', '钓鱼点 - 蒙德', '无妄引咎密宫「祝圣秘境：寒霜」', '债务处理人 - 蒙德', '海渊仙草灵验记', '厄瑞玻斯的秘密 - 岐之试炼', '安提戈努斯', '借景之馆', '慕风蘑菇', '密室大门', '愚人众 - 萤术士 - 璃月', '冰雾花 - 群岛', '精华拜受处', '史莱姆 - 稻妻2', '回声海
螺', '「双双岛」的壁画', '电气水晶 - 璃月', '塞西莉亚花', , '蘑菇 - 璃月', '苹果 - 蒙德', , '遗迹猎者 - 璃月', '风暴后遗症', '白铁矿 - 稻妻', '鱼肉 
- 渊下宫', '晶核 - 龙脊雪山', '雾海纪行 - 日轮与菅名山', '远吕羽氏遗事 · 其三', '深渊法师 - 蒙德', '胡萝卜-群岛', '冒险家...该干嘛', '武者的宿命（后半）', '武器调查点 - 稻妻', ' 
蒙德城的骑士', '芬德尼尔之顶', '翠竹', '夜泊石', '三角的机关', '无想刃狭间 · 磐柱镇石', '蛇心的苏生之辔碎片', '蘑菇 - 稻妻2', '冷杉', '伊达的挑战状', '执望三千里', '螃蟹 - 稻妻', '柳杉 - 孔雀木 - 稻妻', '此菜不应人间有', '海草 - 稻妻', '丘丘岩盔王 - 璃月', '薄荷', '愚人众 - 萤术士 - 蒙德', '池中宅邸', '相位之门 - 鹤观', '烈焰花 - 璃月', '靖世九柱', '清籁
逐雷记 · 其三', '遗迹人形 - 渊下宫', '远吕羽氏遗事 · 其五', '海灵芝 - 稻妻', '海螺 - 鹤观', '离岛之路', '苹果 - 稻妻2', '珊瑚真珠 - 稻妻', '食材调查点', '烈焰花花蕊 - 稻妻', '清 
籁逐雷记 · 其二', '石板 - 鹤观', '孤云凌霄之处「祝圣秘境：惊蛰」', '兽境幼兽 - 鹤观', '轻飘飘的花与芙萝拉', '桦树', '蒙德地灵龛', '清籁旧忆', '盗宝团 - 稻妻', 'NPC商店 - 璃月', '南风之狮的庙宇', '副本', '阵代屋敷', '【木户】与【木奈】', '冰雾花花朵 - 稻妻', '史莱姆 - 璃月', '怀宝应自珍', '玄月宝箱 - 蒙德', '太山宝贝满船归', '肥料推销员', '骗骗花 - 蒙德', '山脊守望「祝圣秘境：不移」', '法厄同们全跳舞', '浪船锚点 - 群岛 破破岛', '圣遗物调查点 - 稻妻', '传送点 - 稻妻 - 海祇岛', '风车菊', '机不可失', '发光髓 - 蒙德', '逐月符 - 蒙德', '掘坟丈夫【蛎罗】', '魔晶矿 - 蒙德', '骗骗花 - 鹤观', '水晶矿 - 璃月', '电气水晶 - 蒙德', '岩神瞳', 'NPC商店 - 稻妻2', '胡萝卜 - 蒙德', '玄月宝箱 - 雪山', '骗骗花 - 稻妻', '蒙 
德-薄荷', '摆设图纸NPC-璃月', '盗宝鼬 - 稻妻', '暂行之策', '白夜国晨昏记-龙蛇洞宫试炼记', '萤火虫 - 稻妻', '木匣 - 鹤观', '凯瑟琳，在稻妻', '薄荷 - 稻妻', '南天门之谜', '晶核 -  
稻妻', , '食材调查点 - 稻妻2', '白萝卜 - 璃月', '鸣神寻踪', '螃蟹 - 稻妻2', '白铁矿 - 群岛', '食莲者', '摆设图纸 - 稻妻', '欢迎来到冒险家协会', '食谱 - 稻妻', '记事 
者之匣', '千里之信', '兽境猎犬 - 鹤观', '七天神像-风', '烈焰花 - 蒙德', '北风之狼的庙宇', '观景点 - 鹤观', '嘟嘟莲', '摆设图纸NPC-蒙德', '松树 - 松木 - 稻妻', '白萝卜 - 稻妻', ' 
丘丘暴徒 - 璃月', , '大伟丘', '【木户】与【木奈】 - 鹤观', '琉璃袋', '祭祀之匣', '笋 - 璃月', '胡萝卜 - 璃月', '蜥蜴尾巴 - 群岛', '丘丘人射手 - 群岛', '清籁逐雷记 · 
其四', '御伽木-稻妻', '突发委托 - 稻妻', '大型丘丘 - 鹤观', '雾海云间寻访记', '晶核 - 鹤观', '岩之印', '蒙德先遣队', '风起风息', '星螺 - 群岛', '青蛙 - 海岛', '漂流瓶 -龙脊雪山', '日月回轮', '堇瓜 - 稻妻2', '大型丘丘人 - 稻妻', '大型丘丘人 - 蒙德', '丘丘萨满 - 蒙德', '武器调查点 - 璃月', '甜甜花', '庙前的苏生之辔碎片', '垂香木 - 蒙德', '广海的守望', '宝 
箱 - 渊下宫', , '书抵万金', '白夜国晨昏记-常世入口', '全能美食队 · 寻食之旅', '马尾 - 璃月', '债务处理人 - 稻妻', '七天神像-岩', '地理志-璃月', '许伯利翁哀歌-狭 
间的叩问', '白铁矿 - 璃月', '琉璃百合', '血斛 - 稻妻', '甜甜花 - 璃月', '深渊法师-群岛', '璃月宝箱', 'NPC奖励 - 蒙德', '宝箱 - 鹤观', '壁画', '松果 - 璃月', '远吕羽氏遗事 · 序', 
'鱼肉 -稻妻2', '梦里生花', '小灯草', '书籍-璃月', , '蛇骨矿洞 · 磐柱镇石', '白铁矿 - 渊下宫', '险恶的教喻', '传送锚点 - 蒙德 - 堕星山谷', '冰雾花 - 蒙德', '观景点 
- 稻妻', '全能美食队·海滩的横行者', '鱼肉 - 稻妻', '丘丘人 - 璃月', '蘑菇 - 海岛', '绀田事话', '萤术士 - 稻妻', '远吕羽氏遗事 · 其四', '椛染之庭', '武者的宿命', '宝箱 - 稻妻', ' 
铁矿 - 稻妻', '摩拉调查点 - 鹤观', '圣遗物调查点', '厄瑞玻斯的秘密 - 八衢彦之试炼', '日落果 - 璃月', '风神瞳', '愚人众 - 债务处理人 - 璃月', '神明啊，我做的对吗', '传送锚点 - 群 
岛 双双岛', '冰雾花', '射手丘丘人 - 鹤观', , '白铁矿 - 鹤观', , '薄荷 - 鹤观', '青蛙 - 璃月', '独木难支', '海贼的标记', '松果 - 鹤观', '蜥蜴尾巴 - 蒙 
德', '岛与海的彼端', '食谱 - 蒙德', '随风到来的好味道', '洗刷耻辱的一战', '雷石', '御伽树 - 御伽木 - 稻妻', '蛇神之首 · 磐柱镇石', '松茸 - 璃月', '低温预警', '钓鱼点 - 稻妻2', ' 
松木 - 璃月', '丘丘萨满 - 鹤观', '神龛', '大雪猪王 - 龙脊雪山', '鱼肉 - 群岛', '璃月港平静的一天', '野蘑菇与公德心【阿部】', '浪船锚点 - 群岛 布丁岛', '蘑菇 - 稻妻', '鳅鳅宝玉 - 
璃月', '探索剑冢封印', '七天神像-风 「蒙德龙脊雪山」', '冒险家罗尔德的日志 · 鹤观', '摆渡人【船工】', '禽肉-璃月 - 蒙德', '林中小书', '书籍 - 龙脊雪山', '社奉行的委任', '简朴的墓
碑', '重岩之意', '丘丘王 - 璃月', , '孤岛诊疗谭', '晶核 - 稻妻2', '浪船锚点 - 群岛 双双岛', '键纹Ⅰ', '白夜国晨昏记-缝隙间的梦', '磨刀不误砍柴工', '某
人的漂流瓶', '射手丘丘人 - 璃月', '绝云椒椒', '孤木孑立，无林可依', '摩拉调查点', '丘丘人 - 海岛', '树莓 - 稻妻2', '七天神像 - 雷', '星螺', '钓鱼点 - 璃月', '在鸣神岛找到长次', '蝴蝶翅膀 - 稻妻', '蜥蜴尾巴 - 璃月', '食材调查点 - 稻妻', '史莱姆 - 稻妻', '华清归藏密宫', '雾海纪行 - 倾听木簧笛的八音曲', '鳅鳅宝玉 - 稻妻', '野伏众 - 稻妻', '蜥蜴尾巴 - 稻妻2', '蘑菇 - 蒙德', 'NPC商店 - 稻妻', '逐月符 - 雪山', '键纹基座Ⅲ', '远吕羽氏遗事 · 其二', '引路仙灵', '天云草实 - 稻妻', '捉迷藏 【音乃】', '陨石碎屑', '矿物调查点 - 稻妻2', '发光 
髓 - 鹤观', '泡泡', '必要手续', '鸣神岛 · 天守', , ' - 蒙德', '紫晶矿 - 鹤观', '渌华景画', '萤术士  - 稻妻', '松茸 - 稻妻', '全能美食队 · 深潜者', '刀剑成梦', '圣遗 
物调查点 - 鹤观', '传送锚点 - 群岛 破破岛', '海草 - 鹤观', '厄瑞玻斯的秘密 - 三隅道大演武', '珊瑚真珠 - 渊下宫', '狂风之核 - 璃月', '蝴蝶翅膀 - 璃月', '无名的宝藏 - 青墟浦', '采 
矿之道', '甜甜花 - 稻妻2', '键纹Ⅴ', '忘却之峡', '「无名岛屿」壁画', '成就【雾里明灯】', '璃月 - 书籍', '承仙所托', '禽肉 - 璃月', '鳗肉 - 鹤观', '健忘大王历险记', '书籍 - 璃月', 
'雪山再勘探', '蛇骨矿洞 · 磐柱镶珠', '丘丘人射手 - 稻妻', '禽肉 - 鹤观', '《第七个武士》', '「危危岛」的壁画', '点亮雷石【知世】', '璃月地灵龛', '外海的蘑菇【阿部】', '飘浮灵 -  
稻妻', '铁矿 - 蒙德', '曲径通幽之处', '全能美食队', '岩晶蝶 - 璃月', '螃蟹 - 群岛', '莲蓬 - 璃月', '千门虚舟', '日落果 - 蒙德', '妖狸 - 稻妻2', '传送锚点 - 璃月 - 琼玑野', '古代 
文明的智慧', '传送锚点 - 群岛 危危岛', '在踏鞴沙找到【长次】', '孔雀木-稻妻', '射手丘丘人 - 稻妻', '食材调查点 - 璃月', '铁矿 - 璃月', '游戏一场', '「破破岛」的壁画', '七天神像- 
雷', '风神与蒙德', '键纹Ⅳ', '飘浮灵 - 鹤观', '魔晶矿 - 稻妻', '钓鱼点 - 鹤观', '键纹基座Ⅳ', '雷神瞳', '金鱼草 - 渊下宫', '自外而来', '海乱鬼 - 稻妻', '孤身犯险', '归乡路漫漫', ' 
海灵芝 - 鹤观', '白夜国晨昏记-奥罗巴洛斯之心', '善后工作', 'NPC奖励 - 稻妻', '鱼肉 - 璃月', '书籍 - 稻妻', '四方八方之网', '逐月符 - 璃月', '落日鳅鳅 - 渊下宫', '蒲公英 - 海岛', 
'诸国游记', '兽肉 - 璃月', , '风后宝矿', '却砂木', '三色档案', '异国的披萨', '矿物调查 - 璃月', '海灵芝', '石匣 - 渊下宫', '金鱼草 - 璃月', '兽肉 - 鹤观', '蜥蜴尾 
巴 - 稻妻', '啊，新鲜的肉！', '键纹Ⅲ', '水晶矿 - 蒙德', '月浴之渊', '大型丘丘人 - 海岛', '捉迷藏【音乃】', '石珀', '踏鞴(bei)物语', '山中之物', '西风之鹰的庙宇', '树莓- 稻妻', ' 
竹笋 - 璃月', '蝴蝶-群岛', '繁忙的冒险家协会', '暂留此影', '松果 - 稻妻', '传送点 - 稻妻 - 清濑岛', '海的那头是故乡', '雾与风的旅行', '【「清籁岛」的记录画片 · 之四】对应拍照点', '星银矿石 - 蒙德', '锈蚀的钥匙', '白夜国晨昏记-寻得龙蛇踪', '狭间的苏生之辔碎片', '完美留影', '冰雾花花朵 - 蒙德', '鱼肉 - 鹤观', '雷石 - 后续出现', '幼岩龙蜥 - 璃月', '鸟蛋', '晶化骨髓 - 稻妻', '愚人众先遣队 - 稻妻', '霓裳花', '鸟蛋 - 璃月', '金属钥匙', '龙蛇藏归辑录', '海上盛珠钿', '遗迹守卫 - 璃月', '蒙德-蘑菇', '遗迹重机 - 稻妻', '镜花听世', '翠石砌玉壶 · 其一/ 翠石砌玉壶 · 其二', '藏镜仕女 - 稻妻', '华池岩岫「祝圣 
玉壶 · 其一/ 翠石砌玉壶 · 其二', '藏镜仕女 - 稻妻', '华池岩岫「祝圣秘境：岩牢」', '栽种之法', '七神的赐福', '尾声，风停之后', '进入「黄金屋」', '远吕羽氏遗事 · 其一', '奇异的牙齿 妻 - 神无冢', '萤火虫 - 璃月', '笔迹已经模糊的笔记', '丘丘人 - 鹤观
 - 龙脊雪山', '绯红玉髓', '书籍 - 蒙德', , '传送点 - 稻妻 - 神无冢', '萤火虫 - 璃月', '笔迹已经模糊的笔记', '丘丘人 - 鹤观', '骗骗花 - 璃月', '盗宝鼬 - 璃月', '浪船  ', '「伏龙树」之底', '丘丘人 - 稻妻', '魔晶矿 - 稻妻2', '羽扇枫-枫 
锚点', , '冰雾花 - 璃月', '羽毛', '许伯利翁哀歌-庙前的叩问\t', '玄月宝箱', '电气水晶 - 稻妻', '烈焰花 - 群岛', '蒲公英籽', '「伏龙树」之底', '丘丘人 - 稻妻', '魔, '键纹基座Ⅴ', '覆雪之国', '晶核 - 渊下宫', '[八重堂」的邀约', '循仙
晶矿 - 稻妻2', '羽扇枫-枫木-稻妻', '兽肉 - 蒙德', '稻妻地灵龛', '董色之庭', '传送锚点 - 璃月 - 璃沙郊', '射手丘丘人 - 蒙德', '宝箱-群岛', '农民的宝藏', '许伯利翁哀歌-蛇心的叩问',盗', '深渊咏者 - 渊下宫', '钓鱼点 - 稻妻', '树莓 - 群岛', '宝箱', '  '传送锚点 - 群岛 布丁岛', '键纹基座Ⅴ', '覆雪之国', '晶核 - 渊下宫', '[八重堂」的邀约', '循仙踪兮天遒', '鹰之门', '清心', '深渊法师 - 鹤观', '丘丘暴徒', '传送点 - 稻妻 - 鸣神岛', ', '太山府「精通秘境：深炎之底」', '【「清籁岛」的记录画片】对应拍  '传送锚点 - 璃月 - 碧水原', '浪船锚点 - 群岛 危危岛', '金鱼草 - 蒙德', '骑士团手册问答', '捕盗', '深渊咏者 - 渊下宫', '钓鱼点 - 稻妻', '树莓 - 群岛', '宝箱', '烹饪的诀窍', '丘丘- 稻妻', '键纹Ⅱ', '白铁矿 - 蒙德', '绯樱绣球 - 稻妻', '在他乡', '树 
萨满 - 璃月', '宝藏归离', , '无明岩 · 磐柱镶珠', '古云有「螭」', '食材调查点 - 蒙德', '遗迹重机 - 蒙德', '传送锚点「蒙德  堕星山谷」 ', '太山府「精通 '璃月幼岩龙蜥', '食谱 - 龙脊雪山', '树莓 - 璃月', '武器调查点 - 稻妻
秘境：深炎之底」', '【「清籁岛」的记录画片】对应拍照点', '全能美食队 · 吃饱的重要性', '鱼群大爆发', '禽肉 - 群岛', '墟散人离之处', '孤舰履孤云', '恨繁囿兮作土', '幽灯蕈 - 鹤观',  ', '【逆子的归乡】触发点', '清籁逐雷记 · 其一', '陨石碎片', '鬼兜虫
'医樱', '松茸 - 鹤观', '丘丘萨满 - 稻妻', '先遣队 - 稻妻', '键纹Ⅱ', '白铁矿 - 蒙德', '绯樱绣球 - 稻妻', '在他乡', '树莓 - 鹤观', '传送锚点 - 渊下宫', '松木 - 蒙德', '【「清籁岛」
的记录画片 · 之三】对应拍照点', , '鸟蛋 - 海岛', '岩龙蜥 - 璃月', '腐殖之牙', '钩钩果', '璃月幼岩龙蜥', '食谱 - 龙脊雪山', '树莓 - 璃月', '武器调查点
 - 稻妻2', '黑岩之困', '传送锚点「蒙德  龙脊雪山」', '冒险要朝着远方', '宝箱 - 龙脊雪山', '苹果 - 璃月', '地灵龛 - 鹤观', '海草 - 稻妻2', '薄荷 - 渊下宫', '踏鞴物语【后续】系列', '落落梅', '【逆子的归乡】触发点', '清籁逐雷记 · 其一', '陨石碎片', '鬼兜虫 - 稻妻', '每天都是新的冒险', '群玉阁....再现？', '「总务司」的事务', '仲夏庭园', '深渊法师 - 璃月']
    """
    return list(set(ret_list) - set())

print(get_all_collection_name())
print()
    