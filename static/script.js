async function uploadImage() {
    const input = document.getElementById("imageInput");
    const resultDiv = document.getElementById("result");

    if (!input.files.length) {
        resultDiv.innerHTML = "Please select an image.";
        return;
    }

    const formData = new FormData();
    formData.append("image", input.files[0]);

    resultDiv.innerHTML = "Analyzing image...";

    const response = await fetch("/analyze", {
        method: "POST",
        body: formData
    });

    const data = await response.json();

    if (!data.is_food) {
        resultDiv.innerHTML = "❌ No food detected in the image.";
    } else {
        resultDiv.innerHTML = `
            🍔 <b>Food:</b> ${data.food}<br>
            📊 <b>Confidence:</b> ${data.confidence}<br>
            🔥 <b>Estimated Calories:</b> ${data.calories}
        `;
    }
}
