require('dotenv').config()

const express = require('express')
const app = express()
const mongoose = require('mongoose')

// connect to the DB
mongoose.connect(process.env.DATABASE_URL, { useNewUrlParser: true })

const db = mongoose.connection
db.on('error', (error) => console.error(error))
db.once('open', () => console.log('Connected to Database'))

// set up server to accept json
app.use(express.json())

// set up routes
const subscribersRouter = require('./routes/subscribers')
app.use('/subscribers', subscribersRouter) // use this whenever we query sunscribers

// server hooked up and listening
app.listen(3000, () => console.log('Server Started'))
