import redis from 'redis';
import { createClient } from 'redis';

const client = createClient();

client.on('error', error => console.log(`Redis client not connected to the server: ${error}`));
client.on('connect', () => console.log('Redis client connected to the server'));

const setNewSchool = (schoolName, value) => {
    client.set(schoolName, value, redis.print);
}

const displaySchoolValue = (schoolName) => {
    client.get(schoolName, (err, obj) => {
        console.log(obj);
    });
}

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
