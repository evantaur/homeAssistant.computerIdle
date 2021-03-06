# homeAssistant.computerIdle
Just a little script that toggles an input boolean based on computer usage.

put idle.exe and config.json in the same directory for it to work.

change values in config.json to match your setup.

{
"url":"<your home assistant URL>/api/states/input_boolean.computer_idle",
"auth":"<Long-Lived Access Token>",
"interval":10, <-- time in seconds between checks
"consider_afk":60  <- time in seconds to consider being idle.
}

i'll rewrite it at some point in C.
