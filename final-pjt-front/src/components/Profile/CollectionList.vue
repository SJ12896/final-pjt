<template>
  <div>
    <ul>
      <CollectionListItem v-for="(collection, idx) in collections" :key="idx" :collection="collection" />
    </ul>
  </div>
</template>

<script>
import CollectionListItem from '@/components/Profile/CollectionListItem.vue'
export default {
  name: 'CollectionList',
  props: {
    collections: Array,
  },
  components: {
    CollectionListItem,
  }
}
</script>

<style>

</style>