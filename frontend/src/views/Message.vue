<template lang="html">
    <div class="single-question mt-2">
        <div class="container">
            <h1>{{ message.content }}</h1>

            <p class="mb-0">Domanda aggiunta da</p>
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
        }
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
                  this.setPageTitle(data.content); //funzione per far si che il title sia uaguale al contenuto del message
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
