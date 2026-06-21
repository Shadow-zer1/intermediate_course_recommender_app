// static/js/script.js

document.addEventListener('DOMContentLoaded', function() {
    // Get references to HTML elements by their IDs
    const recommendationForm = document.getElementById('recommendationForm');
    const bioOrCompRadios = document.querySelectorAll('input[name="bio_or_comp"]');
    const biologyMarksGroup = document.getElementById('biologyMarksGroup');
    const computerMarksGroup = document.getElementById('computerMarksGroup');
    const biologyMarksInput = document.getElementById('biologyMarks');
    const computerMarksInput = document.getElementById('computerMarks');

    const interestCheckboxes = document.querySelectorAll('#interestCheckboxes input[name="interests"]');
    const interestMinWarning = document.getElementById('interestMinWarning');
    const MIN_INTERESTS_SELECTED = 5;

    const careerGoalCheckboxes = document.querySelectorAll('#careerGoalCheckboxes input[name="careerGoals"]');
    const careerGoalMinWarning = document.getElementById('careerGoalMinWarning');
    const careerGoalMaxWarning = document.getElementById('careerGoalMaxWarning');
    const MAX_CAREER_GOALS_SELECTED = 5;
    const MIN_CAREER_GOALS_SELECTED = 1;

    // --- Logic for Biology/Computer Science input visibility ---
    // Ensure initial state is correct if one is pre-selected, or both are hidden
    // Also, ensure the elements exist before trying to access their style
    if (biologyMarksGroup && computerMarksGroup) {
        if (document.getElementById('option_biology') && document.getElementById('option_biology').checked) {
            biologyMarksGroup.style.display = 'block';
            computerMarksGroup.style.display = 'none';
        } else if (document.getElementById('option_computer') && document.getElementById('option_computer').checked) {
            computerMarksGroup.style.display = 'block';
            biologyMarksGroup.style.display = 'none';
        } else {
            biologyMarksGroup.style.display = 'none';
            computerMarksGroup.style.display = 'none';
        }
    } else {
        console.error("Error: 'biologyMarksGroup' or 'computerMarksGroup' not found. Check index.html IDs.");
    }


    bioOrCompRadios.forEach(radio => {
        radio.addEventListener('change', function() {
            if (this.value === 'biology') {
                if (biologyMarksGroup) biologyMarksGroup.style.display = 'block';
                if (computerMarksGroup) computerMarksGroup.style.display = 'none';
                if (computerMarksInput) computerMarksInput.value = '';
                if (biologyMarksInput) biologyMarksInput.focus();
            } else if (this.value === 'computer') {
                if (computerMarksGroup) computerMarksGroup.style.display = 'block';
                if (biologyMarksGroup) biologyMarksGroup.style.display = 'none';
                if (biologyMarksInput) biologyMarksInput.value = '';
                if (computerMarksInput) computerMarksInput.focus();
            }
        });
    });

    // --- Logic for Interest checkbox minimum selection ---
    interestCheckboxes.forEach(checkbox => {
        checkbox.addEventListener('change', function() {
            let checkedCount = 0;
            interestCheckboxes.forEach(cb => {
                if (cb.checked) {
                    checkedCount++;
                }
            });

            if (interestMinWarning) { // Check if element exists
                if (checkedCount < MIN_INTERESTS_SELECTED) {
                    interestMinWarning.style.display = 'block';
                } else {
                    interestMinWarning.style.display = 'none';
                }
            }
        });
    });

    // --- Logic for Career Goal checkbox limit ---
    careerGoalCheckboxes.forEach(checkbox => {
        checkbox.addEventListener('change', function() {
            let checkedCount = 0;
            careerGoalCheckboxes.forEach(cb => {
                if (cb.checked) {
                    checkedCount++;
                }
            });

            if (careerGoalMaxWarning) { // Check if element exists
                if (checkedCount > MAX_CAREER_GOALS_SELECTED) {
                    this.checked = false; // Uncheck the one just clicked
                    careerGoalMaxWarning.style.display = 'block';
                    setTimeout(() => { careerGoalMaxWarning.style.display = 'none'; }, 3000);
                } else {
                    careerGoalMaxWarning.style.display = 'none';
                }
            }
            
            if (careerGoalMinWarning) { // Check if element exists
                if (checkedCount < MIN_CAREER_GOALS_SELECTED) {
                    careerGoalMinWarning.style.display = 'block';
                } else {
                    careerGoalMinWarning.style.display = 'none';
                }
            }
        });
    });


    // --- Form Submission Logic ---
    if (recommendationForm) { // Ensure the form element exists before adding listener
        recommendationForm.addEventListener('submit', async function(event) {
            event.preventDefault();
            console.log('Form submission attempted.');

            // Get values from inputs, adding checks for element existence
            const totalMatricMarksElement = document.getElementById('totalMatricMarks');
            const mathMarksElement = document.getElementById('mathMarks');
            const physicsMarksElement = document.getElementById('physicsMarks');
            const chemistryMarksElement = document.getElementById('chemistryMarks');

            if (!totalMatricMarksElement || !mathMarksElement || !physicsMarksElement || !chemistryMarksElement) {
                console.error("Error: One or more main input elements not found. Check index.html IDs.");
                alert("Missing required input fields. Please ensure the form is loaded correctly.");
                return;
            }

            const totalMatricMarks = parseInt(totalMatricMarksElement.value || 0);
            const mathMarks = parseInt(mathMarksElement.value || 0);
            const physicsMarks = parseInt(physicsMarksElement.value || 0);
            const chemistryMarks = parseInt(chemistryMarksElement.value || 0);
            
            let biologyMarks = 0;
            let computerMarks = 0;
            let bioOrCompOption = '';

            for (const radio of bioOrCompRadios) {
                if (radio.checked) {
                    bioOrCompOption = radio.value;
                    break;
                }
            }

            console.log('Bio/Comp Option Selected:', bioOrCompOption);

            // --- Client-side Validation ---
            if (isNaN(totalMatricMarks) || totalMatricMarks < 0 || totalMatricMarks > 1200) {
                alert('Please enter valid total Matriculation marks (0-1200).');
                console.error('Validation failed: Total Matric marks invalid.');
                return;
            }
            if (isNaN(mathMarks) || mathMarks < 0 || mathMarks > 150 || 
                isNaN(physicsMarks) || physicsMarks < 0 || physicsMarks > 150 || 
                isNaN(chemistryMarks) || chemistryMarks < 0 || chemistryMarks > 150) {
                alert('Mathematics, Physics, and Chemistry marks should be between 0 and 150.');
                console.error('Validation failed: Core subject marks invalid.');
                return;
            }

            if (!bioOrCompOption) {
                alert('Please select whether you took Biology or Computer Science.');
                console.error('Validation failed: Bio/Comp option not selected.');
                return;
            }
            if (bioOrCompOption === 'biology') {
                if (!biologyMarksInput) {
                    console.error("Error: 'biologyMarksInput' not found. Check index.html ID.");
                    alert("Missing Biology marks input field.");
                    return;
                }
                biologyMarks = parseInt(biologyMarksInput.value || 0);
                if (isNaN(biologyMarks) || biologyMarks < 0 || biologyMarks > 150) {
                    alert('Biology marks should be between 0 and 150.');
                    console.error('Validation failed: Biology marks invalid.');
                    return;
                }
            } else if (bioOrCompOption === 'computer') {
                if (!computerMarksInput) {
                    console.error("Error: 'computerMarksInput' not found. Check index.html ID.");
                    alert("Missing Computer Science marks input field.");
                    return;
                }
                computerMarks = parseInt(computerMarksInput.value || 0);
                if (isNaN(computerMarks) || computerMarks < 0 || computerMarks > 150) {
                    alert('Computer Science marks should be between 0 and 150.');
                    console.error('Validation failed: Computer marks invalid.');
                    return;
                }
            }
            
            const selectedInterests = Array.from(interestCheckboxes)
                                        .filter(cb => cb.checked)
                                        .map(cb => cb.value);
            
            const selectedCareerGoals = Array.from(careerGoalCheckboxes)
                                        .filter(cb => cb.checked)
                                        .map(cb => cb.value);

            if (selectedInterests.length < MIN_INTERESTS_SELECTED) {
                alert(`Please select at least ${MIN_INTERESTS_SELECTED} interests.`);
                console.error('Validation failed: Not enough interests selected.');
                return;
            }
            if (selectedCareerGoals.length < MIN_CAREER_GOALS_SELECTED) {
                alert(`Please select at least ${MIN_CAREER_GOALS_SELECTED} career goal.`);
                console.error('Validation failed: Not enough career goals selected.');
                return;
            }
            if (selectedCareerGoals.length > MAX_CAREER_GOALS_SELECTED) {
                 alert(`You can select a maximum of ${MAX_CAREER_GOALS_SELECTED} career goals.`);
                 console.error('Validation failed: Too many career goals selected.');
                 return;
            }

            const requestData = {
                totalMatricMarks: totalMatricMarks,
                mathMarks: mathMarks,
                physicsMarks: physicsMarks,
                chemistryMarks: chemistryMarks,
                bioOrCompOption: bioOrCompOption,
                biologyMarks: biologyMarks,
                computerMarks: computerMarks,
                interests: selectedInterests,
                careerGoals: selectedCareerGoals
            };

            console.log('Sending data to Flask:', JSON.stringify(requestData, null, 2));

            try {
                const response = await fetch('/recommend', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify(requestData)
                });

                if (!response.ok) {
                    const errorText = await response.text();
                    console.error(`HTTP error! status: ${response.status}, response: ${errorText}`);
                    alert(`An error occurred: ${response.status} - ${errorText.substring(0, 150)}... Check console for details.`);
                    throw new Error(`HTTP error! status: ${response.status}`);
                }

                const data = await response.json();
                console.log('Received recommendation:', data);

                const recommendedStreamElement = document.getElementById('recommendedStream');
                const recommendationDetailsElement = document.getElementById('recommendationDetails');
                const resultElement = document.getElementById('result');

                if (recommendedStreamElement && recommendationDetailsElement && resultElement) {
                    recommendedStreamElement.textContent = data.recommendation;
                    recommendationDetailsElement.innerHTML = '';

                    if (data.details && data.details.length > 0) {
                        data.details.forEach(detail => {
                            const li = document.createElement('li');
                            li.textContent = detail;
                            recommendationDetailsElement.appendChild(li);
                        });
                    } else {
                        const li = document.createElement('li');
                        li.textContent = "No specific details available for this recommendation.";
                        recommendationDetailsElement.appendChild(li);
                    }
                    resultElement.style.display = 'block';
                } else {
                    console.error("Error: Result display elements not found. Check index.html IDs.");
                    alert("Could not display recommendation results due to missing HTML elements.");
                }

            } catch (error) {
                console.error('Error fetching recommendation:', error);
                alert('An error occurred while getting your recommendation. Please try again. Check console for network errors.');
            }
        });
    } else {
        console.error("Error: Form element with ID 'recommendationForm' not found.");
    }
});