// Function.js

// Function to apply the fill_class rule to the JSON data
function fillClass(data) {
    // Extracting the array of cases from the 'train' and 'test' properties
    const cases = [...data.train, ...data.test];
  
    // Applying the fill_class rule to each case
    cases.forEach((caseData) => {
      let input = caseData.input[0];
      let output = caseData.output[0];
      let start = null;
      let end = null;
      for (let i = 0; i < input.length; i++) {
        if (input[i] !== output[i]) {
          if (start === null) {
            start = i;
          } else {
            end = i;
            for (let j = start; j <= end; j++) {
              input[j] = output[j];
            }
            start = i;
          }
        }
      }
    });
    return data; // Returning the modified data object
  }
  
  // Function to check if the classification is correct based on the fill_class rule
  function checkClassification(data) {
    let modifiedData = fillClass(data);
    // Extracting the array of cases from the 'train' and 'test' properties
    const cases = [...modifiedData.train, ...modifiedData.test];
    // Checking if each case satisfies the fill_class rule
    for (let caseData of cases) {
      if (caseData.input[0].join("") !== caseData.output[0].join("")) {
        return false;
      }
    }
    return true;
  }
  const Function = {
    fillClass,
    checkClassification,
  };
  export default Function;
  