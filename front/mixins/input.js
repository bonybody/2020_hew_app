export default {
  props: {
    value: {
      type: String | Number,
      default: ''
    }
  },
  computed: {
    inputValue: {
      get() {
        return this.value;
      },
      set(value) {
        this.$emit('input', value);
      }
    },
  },
  methods: {
    raiseEvent: function (event, value) {
      $emit(event, value);
    }
  }
}