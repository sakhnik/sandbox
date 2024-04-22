math.randomseed(os.time())

print "Guess a secret number"

local number = math.random(1000, 9999)

local function count_digits(a)
    local digits = {}
    for i = 0, 9 do
        digits[i] = 0
    end

    local function add_digit(d)
        digits[d] = digits[d] + 1
    end

    add_digit(a % 10)
    add_digit(math.floor(a / 10) % 10)
    add_digit(math.floor(a / 100) % 10)
    add_digit(math.floor(a / 1000))
    return digits
end

local digits = count_digits(number)

-- vim.print(digits)

while true do
    io.write "Your guess: "
    local guess = io.read "*n"
    if guess == number then
        print "Correct!"
        break
    end

    local guess_digits = count_digits(guess)
    local bulls = 0
    for i = 0, 9 do
        if guess_digits[i] > 0 then
            if digits[i] < guess_digits[i] then
                bulls = bulls + digits[i]
            else
                bulls = bulls + guess_digits[i]
            end
        end
    end

    local cows = 0
    if number % 10 == guess % 10 then cows = cows + 1 end
    if math.floor(number / 10) % 10 == math.floor(guess / 10) % 10      then cows = cows + 1 end
    if math.floor(number / 100) % 10 == math.floor(guess / 100) % 10    then cows = cows + 1 end
    if math.floor(number / 1000) == math.floor(guess / 1000)            then cows = cows + 1 end

    print('bulls=' .. bulls .. ' cows=' .. cows)
end
