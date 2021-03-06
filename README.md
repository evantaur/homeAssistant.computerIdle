# homeAssistant.computerIdle
Just a little script that toggles an input boolean based on computer usage.

change values in config.json to match your setup.

{
"url":"<your home assistant URL>/api/states/input_boolean.computer_idle",
"auth":"<Long-Lived Access Token>",
"interval":10, <-- time in seconds between checks
"consider_afk":60  <- time in seconds to consider being idle.
}
