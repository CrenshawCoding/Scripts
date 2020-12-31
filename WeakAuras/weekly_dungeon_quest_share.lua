function(self, event, isInitialLogin, isReloadingUi)
    if(IsInInstance() and IsInGroup())  then
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
        local delay = 0
        while (C_QuestLog.GetInfo(i+1) ~= nil) do
            i = i + 1
            local info = C_QuestLog.GetInfo(i)
            for _, value in pairs(weeklyQuests) do
                if(value == info["title"]) then
                    if(C_QuestLog.IsPushableQuest(info["questID"])) then 
                        C_Timer.After(1*delay, function() 
                                C_QuestLog.SetSelectedQuest(info["questID"]) 
                                QuestLogPushQuest() 
                                print("Sharing "..info["title"]) 
                        end)
                        delay = delay + 10
                    end
                end
            end
        end
    end
    return false
end

