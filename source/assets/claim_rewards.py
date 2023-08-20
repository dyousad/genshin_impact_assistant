from source.manager import asset

ExpeditionReward = asset.Text(zh="探索派遣", en="Expedition Reward")
ClaimDailyCommissionReward = asset.TextTemplate(text={"zh_CN":"每日委托","en_US":"Daily Commission"})
DispatchCharacterOnExpedition = asset.TextTemplate(text={"zh_CN":"探索派遣","en_US":"Dispatch Character"})
ButtonExpeditionMD = asset.Button(threshold=0)
ButtonExpeditionLY = asset.Button(threshold=0)
ButtonExpeditionDQ = asset.Button(threshold=0)
ButtonExpeditionXM = asset.Button(threshold=0)
ButtonExpeditionClaim = asset.Button()
ButtonExpeditionFirstCharacter = asset.Button()
ButtonExpeditionSelectCharacters = asset.Button()
IconExpeditionComplete = asset.ImgIcon()
IconExpeditionComplete2 = asset.ImgIcon()
IconClaimRewardExpedition = asset.ImgIcon()