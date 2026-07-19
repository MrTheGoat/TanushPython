# 🌟 Vision Hunt Registration

A Python program inspired by **Genshin Impact** that simulates the registration process for a fan club. Applicants must pass a series of validation checks before being deemed worthy of receiving a Vision and joining the club.

## 📖 About

This project was created as part of the WiByte Python course, with a Genshin Impact twist.

Instead of a normal registration system, users undergo a Vision eligibility test. If they pass all validation stages, they are granted one of Teyvat's elemental Visions and welcomed into the fan club.

## ✨ Features

- 📝 User registration
- 🔤 Name abbreviation generator
- 💪 Name strength calculation
- ✅ Multi-stage validation
- ⚠️ Exception handling for invalid inputs
- 🌌 Deep validation process
- 🔥 Approval letter

## 🎮 How It Works

1. Enter your registration details.
2. The program validates your information.
3. If all checks are successful, you pass the Vision Trial.
4. You will be chosen to recieve an element on the next full moon
5. Welcome to the Genshin Fan Club!

## 📂 Files

```
welcome_message.py
README.md
```

## 🚀 Running the Project

```bash
python -i secretclub.py
```

## 📚 Concepts Used

- Functions
- Dictionaries
- `*args`
- `**kwargs`
- Assertions
- Exception Handling
- Defensive Programming

## 🛠️ Built With

- Python 3

## 🎯 Future Improvements

- Assign Visions based on personality instead of randomly.
- Save successful applicants to a file.
- Add ranks such as Adventurer, Knight, or Archon.
- Create a GUI version.
- Add achievements and badges.

## 📜 Disclaimer

This is a fan-made educational project inspired by **Genshin Impact** and was created for learning Python. It is not affiliated with or endorsed by HoYoverse.

## ⚙️ Function Format

| Function | Description |
|----------|-------------|
| `short_form(idx, *names, **addons)` | Creates a shortened version of the applicant's name using initials and optional prefixes or suffixes. |
| `name_strength(**fullname)` | Calculates a score based on the provided name fields to determine the applicant's "name strength." |
| `validate(**prelimdata)` | Performs the first stage of validation, checking that all required information has been provided. |
| `deep_validate()` | Runs the final validation stage before deciding whether the applicant is worthy of receiving a Vision. |
| `grant_vision()` | Randomly assigns one of the seven elemental Visions after successful validation. *(Custom function)* |
| `welcome_message()` | Displays the final welcome message, announces the recipient's Vision, and welcomes them to the fan club. *(Custom function)* |