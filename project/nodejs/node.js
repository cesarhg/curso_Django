var io = require('socket.io').listen(8080),//este socket es el principal
	http = require('http'),
	querystring = require('querystring');

io.sockets.on('connection', function(socket){//funcion para enviar mensaje
	socket.on('enviar_mensaje', function(info){
		var values  = querystring.stringify(info);
		var opt = {
			hostname: 'localhost',
			port: '8000',
			path: '/recibir-mensaje/',
			method: 'POST',
			headers: {
				'Content-Type': 'application/x-www-form-urlencoded',
				'Content-Length': values.length
			}
		};
		var request = http.request(opt, function(res){//funcion para recibir mensaje
			res.setEncoding('utf8');
			res.on('data', function(data){
				io.sockets.emit('recibir_mensaje', data);
			});
		});
		request.write(values);
		request.end();
	});
});