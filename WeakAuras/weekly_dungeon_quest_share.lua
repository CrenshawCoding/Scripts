function(self, event, isInitialLogin, isReloadingUi)
    if(IsInInstance())  then
        local weeklyQuests = {"Trading Favors: Halls of Atonement",
            "Trading Favors: Necrotic Wake",
            "Trading Favors: Plaguefall",
            "Trading Favors: Sanguine Depths",
            "Trading Favors: Spires of Ascension",
            "A Valuable Find: Halls of Atonement",
            "A Valuable Find: Necrotic Wake",
            "A Valuable Find: Spires of Ascension",
            "A Valuable Find: Theater of Pain",
        "A Valuable Find: Tirna Scithe"}
        
        -- Share all of the currently active quests in weeklyQuests            
        local activeQuests = {}
        local i = 0
        while (C_QuestLog.GetInfo(i+1) ~= nil) do
            i = i + 1
            local info = C_QuestLog.GetInfo(i)
            for _, value in pairs(weeklyQuests) do
                if(value == info["title"]) then
                    C_QuestLog.SetSelectedQuest(info["questID"])
                    if(C_QuestLog.IsPushableQuest(info["questID"])) then 
                        QuestLogPushQuest()
                        print("Sharing "..info["title"])
                        C_Timer.After(10, QuestLogPushQuest)
                    end
                end
            end
        end
    end
    return false
end

