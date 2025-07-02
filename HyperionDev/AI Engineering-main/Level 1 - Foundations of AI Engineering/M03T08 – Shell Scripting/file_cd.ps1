# insert commands to create three new folders (directories). 
#Name your folders whatever you’d like.
New-Item -ItemType Directory -Name "whatever1"
New-Item -ItemType Directory -Name "whatever2"
New-Item -ItemType Directory -Name "whatever3"

# Array of folder names
$folders = @("whatever1", "whatever2", "whatever3")

# Pick one folder at random
$selectedFolder = Get-Random -InputObject $folders

# insert commands to navigate inside one of the folders you created  
Set-Location -Path $selectedFolder
Write-Output "Navigated into $selectedFolder"

# and create three new folders inside this folder.
New-Item -ItemType Directory -Name "newfolder1"
New-Item -ItemType Directory -Name "newfolder2"
New-Item -ItemType Directory -Name "newfolder3"

# Array of nested folder names
$nestedFolders = @("newfolder1", "newfolder2", "newfolder3")

# Shuffle the array and pick the first two for deletion
$foldersToDelete = $nestedFolders | Get-Random -Count 2

# #Also, insert commands to remove two of the folders you created.
Remove-Item -Recurse -Force $foldersToDelete[0]
Remove-Item -Recurse -Force $foldersToDelete[1]
