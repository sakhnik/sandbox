math.randomseed(os.time())

print "Guess a secret number"

local number = math.random(1000, 9999)
local digits = {}

digits[number % 10] = 1
digits[math.floor(number / 10) % 10] = 1
digits[math.floor(number / 100) % 10] = 1
digits[math.floor(number / 1000)] = 1
--vim.print(digits)

while true do
    io.write "Your guess: "
    local guess = io.read "*n"
    if guess == number then
        print "Correct!"
        break
    end

    local bulls = 0
    if digits[guess % 10] == 1                      then bulls = bulls + 1 end
    if digits[math.floor(guess / 10) % 10] == 1     then bulls = bulls + 1 end
    if digits[math.floor(guess / 100) % 10] == 1    then bulls = bulls + 1 end
    if digits[math.floor(guess / 1000)] == 1        then bulls = bulls + 1 end

    local cows = 0
    if number % 10 == guess % 10 then cows = cows + 1 end
    if math.floor(number / 10) % 10 == math.floor(guess / 10) % 10      then cows = cows + 1 end
    if math.floor(number / 100) % 10 == math.floor(guess / 100) % 10    then cows = cows + 1 end
    if math.floor(number / 1000) == math.floor(guess / 1000)            then cows = cows + 1 end

    print('bulls=' .. bulls .. ' cows=' .. cows)
end
