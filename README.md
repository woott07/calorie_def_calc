# Calorie Deficit Calculator

A simple and interactive Python script to calculate your Basal Metabolic Rate (BMR), Total Daily Energy Expenditure (TDEE), and suggest a daily calorie intake for fat loss based on your personal goals and activity level.

## Features
- **BMR Calculation:** Calculates your Basal Metabolic Rate using your gender, height, weight, and age (using the Harris-Benedict equation).
- **TDEE Calculation:** Estimates your Total Daily Energy Expenditure by applying activity multipliers based on your weekly training frequency.
- **Calorie Deficit Calculation:** Provides a personalized daily calorie target based on three difficulty levels of fat loss:
  - **Easy Fatloss:** 500 kcal daily deficit
  - **Moderate Fatloss:** 750 kcal daily deficit
  - **Hard Fatloss:** 1000 kcal daily deficit

## Requirements
- Python 3.x

## How to Use
1. Ensure you have Python installed on your system.
2. Clone the repository:
   ```bash
   git clone https://github.com/woott07/calorie_def_calc.git
   ```
3. Open a terminal or command prompt in the cloned project directory (`cd calorie_def_calc`).
4. Run the script:
   ```bash
   python def.py
   ```
5. Follow the interactive prompts and enter your details:
   - **Gender:** `M` for Man, `W` for Woman
   - **Height:** Your height in centimeters (cm)
   - **Weight:** Your weight in kilograms (kg)
   - **Age:** Your current age in years
   - **Fatloss Target:** `1` for Easy, `2` for Moderate, `3` for Hard
   - **Training Level:** Valid inputs are `0x`, `1x`, `2x`, `3x`, `4x`, `5x`, `6x`, `7x`, or `14x` depending on how many times you train per week.

## Output
After providing all your inputs, the application will display:
1. Your calculated **BMR**.
2. Your estimated **TDEE**.
3. Your expected **Deficit Input** (which is your daily target calorie intake for your desired fat loss rate).

## License
Feel free to use and modify this script!
