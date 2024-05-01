        n = 0
        for table in tables:  # this section gets entry data from website
            n = n + 1
            for entry in table.find_elements('tag name', 'tr'):
                if entry not in scratched:
                    horse_stats = []
                    new_stat = []
                    for stat in entry.find_elements('tag name', 'td'):
                        stat = stat.text
                        m = stat.replace("\n", "', '").replace(", Jr.", " Jr.")
                        horse_stats.append(m)
                    if horse_stats == []:
                        pass
                    else:
                        npppp = path + "race" + str(n) + "/"
                        new_path = npppp + 'entries.csv'
                        horse_stats_str = str(horse_stats)
                        horse_stats_str = horse_stats_str.replace('"', "'").replace('[', '').replace(']', '').replace("'", '').replace('.', '').replace(' ,', '')
                        horse_stats_str = horse_stats_str[2:]
                        sys.stdout = open(new_path, 'a')
                        print(horse_stats_str)
                else:
                    pass
                    
                    
        # for each entry
        # for each entry that is not scratched 
        # for each stat in entry, we need to string together the info for each entry
        # turn all stats into individual elements for easy access, ei. [1],[2],[3],etc
        # then turn all into strings and write to csv file
        
        