#Title
Write-Host "SMART GOAL"
Write-Host "Input specific information about desired goal"
#SMART GOAL Input
$GoalTitle = Read-Host -Prompt "What's your goal?"
$Specific = Read-Host -Prompt " Get clear: What do you need to focus on speficially?"
$Measure = Read-Host -Prompt "How will you measure this?"
$Achieve = Read-Host -Prompt "Is this achievable? Y/N"
$Relevant = Read-Host -Prompt "Is this relevant? Y/N"
$Time = Read-Host -Prompt "How many days are you giving yourself?"
"`r`n"

$Smarr = @($GoalTitle,$Specific,$Measure,$Achieve,$Relevant,$Time)


Write-Host "Goal:" $GoalTitle
"`r`n"
Write-Host "Specific:" $Specific
Write-Host "Measurable:" $Measure
Write-Host "Achievable:" $Achieve
Write-Host "Relevant:" $Relevant
Write-Host "Time:" $Time
"`r`n"
if ($Achieve -ne "y"){Write-Host "Rewrite goal to be achievable"
}
if ($Relevant -ne "y"){Write-Host "Rewrite goal to be relevant"
}

$Save = Read-Host -Prompt "Do you want to make a textfile to save this goal? Y/N"
"`r`n"
if($Save -eq "n"){Write-Host "Copy and paste into a txt or csv file. Good Luck!"
}elseif($Save -eq "y"){New-Item -Path C:/Users/user/Desktop/ -Name GoalSheet.txt -ItemType File
}else{Write-Host "Invalid Input: y or n please"}


#Foreach Array - Remember to change directory
$Smarr | Out-File -Append c:/Users/user/Desktop/GoalSheet.txt 


Write-Host "Best of Luck with SMART Goal! Your goal is important. Find accountability."
