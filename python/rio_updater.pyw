import time

import requests
import os
import datetime

update_alliance = True

db_dir = r'C:\Program Files (x86)\World of Warcraft\_retail_\Interface\AddOns\RaiderIO\db'
log_path = r'C:\Program Files (x86)\World of Warcraft\_retail_'
base_path = 'https://raw.githubusercontent.com/RaiderIO/raiderio-addon/master/db/'
files = ['db_mythicplus_eu_lookup.lua',
         'db_mythicplus_eu_characters.lua',
         'db_raiding_eu_lookup.lua',
         'db_raiding_eu_characters.lua',
         'db_recruitment_eu_characters.lua',
         'db_realms.lua',
         'db_recruitment_eu_lookup.lua',
         'db_score_tiers.lua',
         'db_score_stats.lua']

# --- Deprecated ---:
files_horde = ['db_eu_horde_characters.lua',
               'db_eu_horde_lookup.lua',
               'db_raiding_eu_horde_characters.lua',
               'db_raiding_eu_horde_lookup.lua',
               'db_recruitment_eu_horde_characters.lua',
               'db_recruitment_eu_horde_lookup.lua']
files_alliance = ['db_eu_alliance_characters.lua',
                  'db_eu_alliance_lookup.lua',
                  'db_raiding_eu_alliance_characters.lua',
                  'db_raiding_eu_alliance_lookup.lua',
                  'db_recruitment_eu_alliance_characters.lua',
                  'db_recruitment_eu_alliance_lookup.lua'
                  ]
# ---
log_file = open(os.path.join(log_path, 'rio_log.txt'), 'w+')


def end_on_excessive_retries(retries):
    if retries > 5:
        log_file.write("Too many retries, exiting")
        quit()


def get_timestamp():
    now = datetime.datetime.now()
    return now.strftime('%d.%m.%y %H:%M:%S.%f')[:-3]  # this format gets 3 decimal places of milliseconds


# TODO: Rewrite, as there is only one file list now
def write_to_file(file_name: str):
    log_file.write(get_timestamp() + '\tRequesting ' + file_name + '\n')
    r = requests.get(base_path + file_name)
    retry_counter = 0
    while retry_counter < 3 and (r.status_code != 200 or len(r.content) == 0):
        time.sleep(5)
        log_file.write("Retrying for " + file_name)
        r = requests.get(base_path + file_name)
        retry_counter += 1
    if r.status_code == 200 and len(r.content) > 0:
        log_file.write(get_timestamp() + '\tWriting ' + file_name + '\n')
        f = open(os.path.join(db_dir, file_name), 'w', encoding='utf8')
        f.write(r.content.decode())
    return retry_counter


try:
    retries = 0
    counter = 1
    if update_alliance:
        for file in files:
            print('Progress: {0}/{1}'.format(counter, len(files)))
            counter = counter + 1
            write_to_file(file)
            end_on_excessive_retries(retries)
except Exception as e:
    log_file.write(repr(e))
