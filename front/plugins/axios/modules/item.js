export default class Item {
  constructor(axios) {
    this.api = axios;
    this.prefix = '/item/';
    console.log(this.api);
  }

  async getById(id, user_id) {
    const res = await this.api.get(this.prefix, {
      params: {
        id: id,
        user_id: user_id
      }
    })
    return res
  }
  async getItemsByUserId(user_id) {
    const res = await this.api.get(this.prefix + 'user', {
      params: {
        user_id: user_id
      }
    })
    return res
  }
  async getNewItems(user_id) {
    const res = await this.api.get(this.prefix + 'new', {
      params: {
        user_id: user_id
      }
    })
    return res
  }

  async getFavoriteItems(user_id) {
    const res = await this.api.get(this.prefix + 'favorite', {
      params: {
        user_id: user_id
      }
    })
    return res
  }


  async post(params) {
    this.api.setHeader('Content-Type', 'multipart/form-data')
    this.api.setHeader('Accept', 'application/json')
    console.log(params);
    const res = await this.api.post(this.prefix, params);
    console.log(res);
    return res
  }
}