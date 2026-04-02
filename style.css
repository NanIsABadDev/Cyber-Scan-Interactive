function update() {
    // Gerar dados aleatórios
    const ip = `${r(255)}.${r(255)}.${r(255)}.${r(255)}`;
    const port = [80, 443, 8080, 22, 21, 3306][Math.floor(Math.random() * 6)];
    const ping = Math.floor(Math.random() * 80) + 5;
    const percent = Math.floor(Math.random() * 101);
    
    // Status aleatório
    const messages = ["CONNECTED", "SCANNING", "BYPASSING", "UPDATING", "ENCRYPTED"];
    const status = messages[Math.floor(Math.random() * messages.length)];

    // Atualizar HTML
    document.getElementById('ip').innerText = ip;
    document.getElementById('port').innerText = port;
    document.getElementById('ping').innerText = ping + " MS";
    document.getElementById('speed').innerText = status;
    document.getElementById('percent').innerText = percent + "%";
    
    // Atualizar barra
    document.getElementById('bar').style.width = percent + "%";
}

function r(max) {
    return Math.floor(Math.random() * max);
}

// Atualiza automaticamente a cada 3 segundos
setInterval(update, 3000);

// Executa ao carregar a página
window.onload = update;
