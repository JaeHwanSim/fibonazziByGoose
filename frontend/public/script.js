document.getElementById('fib-form').addEventListener('submit', async function(event) {
    event.preventDefault();

    const numberInput = document.getElementById('number');
    const resultP = document.getElementById('result');
    const timestampP = document.getElementById('timestamp');
    const sequenceP = document.getElementById('sequence');
    const errorContainer = document.getElementById('error-container');

    const n = parseInt(numberInput.value, 10);

    // Clear previous results and errors
    resultP.textContent = '';
    timestampP.textContent = '';
    sequenceP.textContent = '';
    errorContainer.textContent = '';

    // Frontend Validation
    if (isNaN(n) || n < 0 || n > 100) {
        errorContainer.textContent = '오류: 0에서 100 사이의 숫자를 입력해주세요.';
        return;
    }

    try {
        const response = await fetch('/api/calculate', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ number: n }),
        });

        if (!response.ok) {
            const errorData = await response.json();
            // Try to parse a meaningful error message from the backend
            let message = '알 수 없는 오류가 발생했습니다.';
            if (errorData.detail && Array.isArray(errorData.detail) && errorData.detail.length > 0) {
                message = errorData.detail[0].msg;
            } else if (errorData.detail) {
                message = errorData.detail;
            }
            throw new Error(message);
        }

        const data = await response.json();
        
        // Display results
        resultP.textContent = `피보나치(${n}) = ${data.result}`;
        timestampP.textContent = new Date().toLocaleString('ko-KR');
        sequenceP.textContent = data.sequence.length > 0 ? data.sequence.join(', ') : 'N/A';

    } catch (error) {
        errorContainer.textContent = `오류: ${error.message}`;
    }
});
