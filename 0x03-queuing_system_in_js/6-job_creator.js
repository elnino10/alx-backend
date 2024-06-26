import { createQueue } from "kue";

const queue = createQueue();

const jobDataFormat = {
    phoneNumber: '08036943113',
    message: 'The first phone number',
}

const job = queue.create('push_notification_code', jobDataFormat)
job.on('enqueue', () => {
    console.log(`Notification job created: ${job.id}`);
}).on('failed attempt', () => {
    if (error) console.log('Notification job failed');
}).on('completed', () => {
    console.log('Notification job completed');
})

job.save();
