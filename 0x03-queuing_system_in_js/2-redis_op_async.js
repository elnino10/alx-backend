import redis from 'redis';
import { promisify } from 'util';
import { createClient } from 'redis';

const client = createClient();
const getAsync = promisify(client.get).bind(client);

client.on('error', error => console.log(`Redis client not connected to the server: ${error}`));
client.on('connect', () => console.log('Redis client connected to the server'));

const setNewSchool = (schoolName, value) => {
    client.set(schoolName, value, redis.print);
}

const displaySchoolValue = async (schoolName) => {
    const value = await getAsync(schoolName);
    console.log(value);
}

(async () => {
    await displaySchoolValue('Holberton');
    setNewSchool('HolbertonSanFrancisco', '100');
    await displaySchoolValue('HolbertonSanFrancisco');
})()
