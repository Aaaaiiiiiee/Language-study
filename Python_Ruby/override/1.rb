class C1
    def m()
        return 'parent'
    end
end

class C2 < C1
    def m()
        return super() + ' child'
    end
end

c = C2.new()
p c.m()

# Python에서 super()는 부모 클래스 객체를
# Ruby에서 super()는 부모 클래스의 override한 메소드를 가리킨다.