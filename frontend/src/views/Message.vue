<template lang="html">
    <div class="single-question mt-2">
        <div class="container">
            <h1>{{ message.content }}</h1>
            <!-- <iframe> {{ message.cover }}</iframe> -->
            <span> {{ message.cover }}</span>

            <p class="mb-0">Messaggio aggiunto da</p>
                <span class="author_name">{{ message.author }}</span>
            </p>
            <p>{{ message.created_at }}</p>
            <hr>
        </div>
    </div>
</template>

<script>
import { apiService } from "../common/api.service";
export default {
    name: "Message",

    props: {
        slug:{
            type: String,
            required: true
        },
        // pk:{
        //     type: String,
        //     required: true
        // },

    },

    data() {
        return {
            message: {}
        }
    },

    methods: {
        setPageTitle(title) {
            document.title= title;
        },

        getMessageData() {
            let endpoint = `/api/messagestext/${this.slug}/`;
            apiService(endpoint)
                .then(data => {
                  this.message = data;
                  this.setPageTitle(data.content); //funzione per far si che il title sia uguale al contenuto del message
                })
        }
    },

    created(){
       this.getMessageData();
    }
}
</script>

<style lang="css" scoped>


</style>
