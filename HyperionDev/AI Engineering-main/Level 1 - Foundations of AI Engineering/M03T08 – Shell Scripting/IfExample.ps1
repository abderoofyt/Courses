# Write an if statement to create a new folder named if_folder 
# if a folder named new_folder already exists.
if (Test-Path "new_folder") {
    New-Item -ItemType Directory -Name "if_folder"
}

# Within the same file, write an if-else statement to check 
# whether a folder named if_folder exists.
if (Test-Path "if_folder") {
    # If it does, create a new folder named hyperionDev 
    New-Item -ItemType Directory -Nam e "hyperionDev"
} else {
    # otherwise, create a new folder named new-projects.
    New-Item -ItemType Directory -Name "new-projects"
}
