# PowerShell Script to Check Password Strength

function Test-PasswordStrength {
    param (
        [Parameter(Mandatory=$true)]
        [string]$Password
    )

    # Initialize strength score
    $strengthScore = 0

    # Check password length
    if ($Password.Length -ge 12) {
        $strengthScore += 3
    } elseif ($Password.Length -ge 8) {
        $strengthScore += 2
    } elseif ($Password.Length -ge 6) {
        $strengthScore += 1
    }

    # Check for uppercase letters
    if ($Password -cmatch '[A-Z]') {
        $strengthScore += 1
    }

    # Check for lowercase letters
    if ($Password -cmatch '[a-z]') {
        $strengthScore += 1
    }

    # Check for numbers
    if ($Password -match '\d') {
        $strengthScore += 1
    }

    # Check for special characters
    if ($Password -match '[\W_]') {
        $strengthScore += 2
    }

    # Determine password strength based on score
    if ($strengthScore -ge 7) {
        $strength = "Strong"
    } elseif ($strengthScore -ge 5) {
        $strength = "Moderate"
    } else {
        $strength = "Weak"
    }

    # Return the strength result
    return @{
        Password = $Password
        Strength = $strength
        Score = $strengthScore
    }
}

# Prompt the user to enter a password
$password = Read-Host "Enter a password to check its strength"

# Test the password strength
$result = Test-PasswordStrength -Password $password

# Output the result
Write-Host "Password: $($result.Password)"
Write-Host "Strength: $($result.Strength)"
Write-Host "Score: $($result.Score)"