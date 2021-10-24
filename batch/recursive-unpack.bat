:: To actually include the path expansion character (tilde), I had to give valid numbers; see http://ss64.com/nt/rem.html for bug reference. Also, try call /? for more info.
@REM The %~n0 extracts the name sans extension to use as output folder. If you need full paths, use "%~dpn0". The -y forces overwriting by saying yes to everything. Or use -aoa to overwrite.
@REM Using `x` instead of `e` maintains dir structure (usually what we want)
set baseFolder="G:\For All Mankind\S02"
@FOR /R %%a IN (*.rar) DO @(
    @if [%1] EQU [/y] (
        @7z e "%%a" -o^"%baseFolder%" -aoa
    ) else (
        @echo 7z e "%%a" -o^"%baseFolder%^" -aoa
    )
)

@echo USAGE: Use /y to actually do the extraction