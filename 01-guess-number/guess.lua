print "Guess my number from 1 to 100"

math.randomseed(os.time())

local num = math.random(100)

while true do
    io.write "Your guess: "
    local guess = io.read "*n"
    if guess == num then
        print "Correct!"
        break
    elseif guess < num then
        print "Too small"
    else
        print "Too big"
    end
end
